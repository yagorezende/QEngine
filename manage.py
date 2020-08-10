"""
Call this script to initialize the application
"""
import argparse

from kivy.lang import Builder

import views.MainPaneApp as mp

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Call this file parsing the option to operate.', prog="QEngine")
    # TODO: Build application for release
    parser.add_argument('-b', "--build", action='store_true',
                        default=False,
                        help='Build the application for release')

    args = parser.parse_args()
    if(args.build):
        print("TODO build")
    else:
        mp.QEngineApp().run()