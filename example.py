#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import random
import sys
import time

sys.path.append(os.path.join(sys.path[0], 'src'))

from check_status import check_status
from feed_scanner import feed_scanner
from follow_protocol import follow_protocol
from instabot import InstaBot
from unfollow_protocol import unfollow_protocol


class InstaBot2(InstaBot):

    def run(self):

        # ------------------- Get media_id -------------------
        if len(self.media_by_tag) == 0:
            self.get_media_id_by_tag(random.choice(self.tag_list))
            self.this_tag_like_count = 0
            self.max_tag_like_count = random.randint(
                1, self.max_like_for_one_tag)
        # ------------------- Like -------------------
        print("[Trying to like]")
        self.new_auto_mod_like()
        # ------------------- Follow -------------------
        print("[Trying to follow]")
        self.new_auto_mod_follow()
        # ------------------- Unfollow -------------------
        # self.new_auto_mod_unfollow()
        # ------------------- Comment -------------------
        print("[Trying to Comment]")
        self.new_auto_mod_comments()
        # Bot iteration in 1 sec
        print("[Stop we gonna sleep]")
        time.sleep(3)
            # print("Tic!")


ACCOUNTS = [
    {
        'username': 'jakarumana',
        'password': 'master88',
    },
    {
        'username': 'vivilutfiahshakeera',
        'password': 'master88',
    },

]
bots = []
for account in ACCOUNTS:
    bot = InstaBot2(
        login=account['username'],
        password=account['password'],
        like_per_day=1000,
        comments_per_day=50,
        tag_list=['hijab', 'addavii'],
        tag_blacklist=['rain', 'thunderstorm'],
        user_blacklist={},
        max_like_for_one_tag=50,
        follow_per_day=300,
        follow_time=1 * 60,
        unfollow_per_day=0,
        unfollow_break_min=15,
        unfollow_break_max=30,
        log_mod=0,
        proxy='',
        # List of list of words, each of which will be used to generate comment
        # For example: "This shot feels wow!"
        comment_list=[["this", "the", "your"],
                      ["photo", "picture", "pic", "shot", "snapshot"],
                      ["is", "looks", "feels", "is really"],
                      ["great", "super", "good", "very good", "good", "wow",
                       "WOW", "cool", "GREAT","magnificent", "magical",
                       "very cool", "stylish", "beautiful", "so beautiful",
                       "so stylish", "so professional", "lovely",
                       "so lovely", "very lovely", "glorious","so glorious",
                       "very glorious", "adorable", "excellent", "amazing"],
                      [".", "..", "...", "!", "!!", "!!!"]],
        # Use unwanted_username_list to block usernames containing a string
        ## Will do partial matches; i.e. 'mozart' will block 'legend_mozart'
        ### 'free_followers' will be blocked because it contains 'free'
        unwanted_username_list=[
            'second', 'stuff', 'art', 'project', 'love', 'life', 'food', 'blog',
            'free', 'keren', 'photo', 'graphy', 'indo', 'travel', 'art', 'shop',
            'store', 'sex', 'toko', 'jual', 'online', 'murah', 'jam', 'kaos',
            'case', 'baju', 'fashion', 'corp', 'tas', 'butik', 'grosir', 'karpet',
            'sosis', 'salon', 'skin', 'care', 'cloth', 'tech', 'rental', 'kamera',
            'beauty', 'express', 'kredit', 'collection', 'impor', 'preloved',
            'follow', 'follower', 'gain', '.id', '_id', 'bags'
        ],
        unfollow_whitelist=['example_user_1', 'example_user_2'])

    bots.append(bot)

# while True:

    #print("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print("## MODE 1 = MODIFIED MODE BY KEMONG")
    #print("### MODE 2 = ORIGINAL MODE + UNFOLLOW WHO DON'T FOLLOW BACK")
    #print("#### MODE 3 = MODIFIED MODE : UNFOLLOW USERS WHO DON'T FOLLOW YOU BASED ON RECENT FEED")
    #print("##### MODE 4 = MODIFIED MODE : FOLLOW USERS BASED ON RECENT FEED ONLY")
    #print("###### MODE 5 = MODIFIED MODE : JUST UNFOLLOW EVERYBODY, EITHER YOUR FOLLOWER OR NOT")

    ################################
    ##  WARNING   ###
    ################################

    # DON'T USE MODE 5 FOR A LONG PERIOD. YOU RISK YOUR ACCOUNT FROM GETTING BANNED
    ## USE MODE 5 IN BURST MODE, USE IT TO UNFOLLOW PEOPLE AS MANY AS YOU WANT IN SHORT TIME PERIOD

if __name__ == '__main__':
    mode = 6
    if mode == 0:
        bot.bot_follow_list = ['addavii', 'marwashania']
        bot.new_auto_mod()

    elif mode == 1:
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10 * 60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) < 50:
                feed_scanner(bot)
                time.sleep(5 * 60)
                follow_protocol(bot)
                time.sleep(10 * 60)
                check_status(bot)

    elif mode == 2:
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3:
        unfollow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 4:
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10 * 60)

    elif mode == 5:
        bot.bot_mode = 2
        unfollow_protocol(bot)

    elif mode == 6:
        print("Masuk mode 6")
        # users = ['addavii', 'marwashania', '000studio']
        # while len(users) > 0:
        for bot in bots:
            print("BOT :", bot.user_id)
            # bot.follow(users.pop())
            bot.run()
        s = random.randint(30,60)
        time.sleep(s)
        print("Waktunya tidur % detik" % s)

    else:
        print("Wrong mode!")
