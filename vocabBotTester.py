import vocabBot
import time

while True:
    time.sleep(60)
    robot=vocabBot.vocabBot()
    robot.proccessMentions()