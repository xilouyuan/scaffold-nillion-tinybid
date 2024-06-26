from nada_dsl import *


def nada_main():
    # Create the voter parties and the voting official party.
    bidders: list[Party] = []
    winners: list[SecretInteger] = []
    for i in range(4):
        bidders.append(Party("bidder" + str(i)))
    official = Party(name="official")
    bidding_prices = [SecretInteger(Input(name="bidder" + str(i), party=bidders[i])) for i in range(4)]
    winner_price = bidding_prices[0]
    for i in range(1, 4):
        condition = bidding_prices[i] > winner_price
        winner_price = condition.if_else(bidding_prices[i], winner_price)

    for i in range(0, 4):
        winners.append((winner_price == bidding_prices[i]).if_else(Integer(1), Integer(0)))

    outputs: list[Output] = [Output(winner_price, "winner_price", official)]
    for i in range(4):
        outputs.append(Output(winners[i], "bidder" + str(i), official))

    return outputs


