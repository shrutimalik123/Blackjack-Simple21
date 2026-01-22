import random

def play_blackjack():
    # 1. Setup the deck
    # In this simple version, we use numbers 2-11 (11 is an Ace)
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    random.shuffle(deck)

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("--- 🃏 Simple Blackjack (21) 🃏 ---")

    # 2. Player Turn
    while True:
        player_score = sum(player_hand)
        print(f"\nYour hand: {player_hand} (Total: {player_score})")
        print(f"Dealer's visible card: [{dealer_hand[0]}]")

        if player_score > 21:
            print("💥 BUST! You went over 21.")
            return

        choice = input("Do you want to [H]it or [S]tand? ").lower().strip()

        if choice == 'h':
            player_hand.append(deck.pop())
        elif choice == 's':
            break

    # 3. Dealer Turn
    print("\n--- Dealer's Turn ---")
    while sum(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    
    dealer_score = sum(dealer_hand)
    print(f"Dealer's final hand: {dealer_hand} (Total: {dealer_score})")

    # 4. Final Comparison
    if dealer_score > 21:
        print("🎉 Dealer busted! YOU WIN!")
    elif player_score > dealer_score:
        print("🎉 You beat the dealer! YOU WIN!")
    elif player_score < dealer_score:
        print("📉 Dealer wins. Better luck next time!")
    else:
        print("🤝 It's a draw (Push)!")

# Start the game
play_blackjack()
