import pandas as pd
import praw
import os
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("--client_id", type=str)
parser.add_argument("--client_secret", type=str)
parser.add_argument("--user_agent", type=str, default='get body text for the comment')
parser.add_argument("--output_dir", type=str, default='raw_data_with_text')

args = parser.parse_args()

reddit = praw.Reddit(client_id=args.client_id, client_secret=args.client_secret, user_agent='next_sentence_prediction')


def get_response(reddit_id):
  result = None
  if reddit_id.startswith('t1'):
    try:
      comment = reddit.comment(id=reddit_id[3:])
      result = comment.body
    except:
      pass
  elif reddit_id.startswith('t3'):
    try:
      comment = reddit.submission(id=reddit_id[3:])
      result = comment.title
    except:
      pass

  return result


def build_dataset(input_csv, output_csv, dry_run=False):
  reddit_df = pd.read_csv(input_csv).dropna()
  print(len(reddit_df))
  if dry_run:
    reddit_df = reddit_df[:100]
  reddit_ids = reddit_df['id'].values

  all_text = []

  for reddit_id in tqdm(reddit_ids):
    instance_text = get_response(reddit_id)
    if instance_text: 
      instance_text = instance_text.replace("\r", "\n") # Fix bug with broken rows in the dataframe
    all_text.append(instance_text)

  reddit_df['body'] = all_text
  reddit_df.to_csv(output_csv, index=False)


def main():
  os.makedirs(args.output_dir, exist_ok=True)
  train_csv_in = 'raw_data/train.csv'
  train_csv_out = os.path.join(args.output_dir, 'train.csv')
  build_dataset(train_csv_in, train_csv_out)

  val_csv_in = 'raw_data/val.csv'
  val_csv_out = os.path.join(args.output_dir, 'val.csv')
  build_dataset(val_csv_in, val_csv_out)

  test_csv_in = 'raw_data/test.csv'
  test_csv_out = os.path.join(args.output_dir, 'test.csv')
  build_dataset(test_csv_in, test_csv_out)


if __name__ == '__main__':
  main()
