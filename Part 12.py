
    clock = pygame.time.Clock()

    time = 0  # In Seconds

    # GameLoop

    while True:
        milli = clock.tick()  # clock.tick() returns how many milliseconds passed since the last time it was called

        # So it tells you how long the while loop took

        seconds = milli / 1000.

        time += seconds

        print
        time  # So you can see that this works
#counts up