import numeric_model
import logging as log


def main():
    if __name__ == '__main__':
        log.basicConfig(filename="critical.log", level=log.CRITICAL)
        mod = numeric_model.NumericModel("resources/plot.dat", low_x=80, low_y=50, max_x=280, max_y=200, cut=True)
        mod.start_model_processing()

main()