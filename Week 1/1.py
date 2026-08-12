def launch_rocket(count):
    if count >= 1:
        print(count)
        launch_rocket(count - 1)

launch_rocket(10)
print('🚀🚀🚀')