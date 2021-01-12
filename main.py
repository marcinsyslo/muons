import numeric_model


if __name__ == '__main__':
    mod = numeric_model.NumericModel("resources/plot.dat", low_x=80, low_y=50, max_x=280, max_y=200, cut=True)
    mod.mod_import()
