from PaperPurchaseAgent import PaperPurchaseAgent
from PaperPurchaseEnvironment import PaperPurchaseEnvironment
from PlotPrices import PlotPrices


def main():
    env = PaperPurchaseEnvironment()
    ag = PaperPurchaseAgent(env)
    ag.go(90)

    pl = PlotPrices(ag, env)
    pl.plot_run()


if __name__ == "__main__":
    main()
