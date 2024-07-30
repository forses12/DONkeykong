import pygame, time, view, model, controller



while True:
    time.sleep(1/550)
    controller.control()
    model.model()
    view.view()
