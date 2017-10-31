from instapy import InstaPy
import argparse
import json
from pprint import pprint

print("PLEASE BE SURE YOU HAVE ALREADY SET UP THE FILE settings.json BEFORE STARTING THIS")

##json file

parser = argparse.ArgumentParser(description='Instagram bot with python')
parser.add_argument('-u','--username', help='Instagram username', action="store", dest="username", required=True)
parser.add_argument('-p','--password', help='Instagram password', action="store", dest="password", required=True)
parser.add_argument('-un', help='the amount of users to unfollow', action='store_true', default=False, dest='unfollow_flag')
parser.add_argument('-f', help='the amount of users to follow', action='store_true', default=False, dest='follow_flag')
parser.add_argument('-c', help='set comments', action='store_true', default=False, dest='comment_flag')
parser.add_argument('-j','--json', help='Json configuration file', action='store', default='settings.json', dest='json')

args = parser.parse_args()


###json
with open(args.json) as settings_file:
    settings = json.load(settings_file)

follower_limit = settings["general_settings"][0]["user_follower_limit"]
nogui = settings["general_settings"][0]["no_gui"]

#comments
comment_settings = settings["general_settings"][0]["comments_settings"][0]
comments = comment_settings["comments"]
comment_tags = comment_settings["comment_tags"]
comment_percentage = comment_settings["comment_percentage"]
comment_amount = comment_settings["comment_amount"]
comment_media = comment_settings["comment_media"]

#follow
follow_settings = settings["general_settings"][0]["follow_settings"][0]
users_followers = follow_settings["follow_user_followers"]
follow_percentage = follow_settings["follow_percentage"]
follow_random = follow_settings["follow_random"]
follow_delay = follow_settings["follow_delay"]
follow_amount = follow_settings["follow_amount"]

#unfollow
unfollow_settings = settings["general_settings"][0]["unfollow_settings"][0]
unfollow_amount = unfollow_settings["unfollow_amount"]
unfollow_method = unfollow_settings["unfollow_method"]
unfollow_delay = unfollow_settings["unfollow_delay"]

insta_username = args.username
insta_password = args.password

session = InstaPy(username=args.username, password=args.password, nogui=nogui)
session.login()

session.set_upper_follower_count(limit=follower_limit)

if args.comment_flag:
    session.set_do_comment(True, percentage=comment_percentage)
    session.set_comments(comments, media=comment_media)
    session.like_by_tags(comment_tags, amount=comment_amount)

if args.follow_flag:
    session.set_do_follow(enabled=True, percentage=follow_percentage, times=1)
    session.follow_user_followers(users_followers, amount=follow_amount, random=follow_random, sleep_delay=follow_delay)


if args.unfollow_flag:
    session.unfollow_users(amount=unfollow_amount, onlyInstapyMethod = unfollow_method, sleep_delay=unfollow_delay )

session.end()
