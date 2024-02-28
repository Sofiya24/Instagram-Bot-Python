from instabot import Bot
bot = Bot()
bot.login(username="sofiya_2404",password="Sofiya@1319")
bot.follow("sofiya_2404")


bot.upload_photo("ai_image.jpeg")


bot.unfollow('learn_ingnewtech')


bot.send_message("How is my photo",["leo.ediz_"])


followers = bot.get_user_followers("sofiya_2404")
for follower in followers:
    print(bot.get_user_info(follower))



following = bot.get_user_following("sofiya_2404")
for Following in following:
    print(bot.get_user_info(Following))