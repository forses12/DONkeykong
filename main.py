import pygame, time, view, model, controller



while True:
    time.sleep(1/550)
    model.model()
    controller.control()
    view.view()
