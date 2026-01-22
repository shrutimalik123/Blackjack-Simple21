# 🃏 Simple Blackjack (21) - Python Edition

A console-based version of the classic casino card game. This simulator features a full shuffled deck, a player turn system, and an automated dealer that follows standard casino rules (hitting until reaching 17). 

This project focuses on teaching:
* **The `sum()` Function:** Efficiently calculating totals from a dynamic list of items.
* **Function Flow Control:** Using `return` to exit a game early upon a "Bust."
* **Loop-Based AI:** Programming a dealer to make decisions based on specific value thresholds.
* **List Manipulation:** Using `.pop()` to remove cards from a deck and `.append()` to add them to a hand.

---

## ✨ Features

* **Full Deck Simulation:** Uses a 52-card deck (values 2-11) shuffled randomly.
* **Automated Dealer:** The dealer logic is programmed to "Stand" only once they hit a total of 17 or higher.
* **Real-time Scoring:** Displays your total and the dealer's visible card after every "Hit."
* **End-Game Logic:** Automatically handles Wins, Losses, Busts, and Draws (Pushes).

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `blackjack.py`.
2.  **Open Terminal:** Navigate to your project folder.
3.  **Run the Script:**
    ```bash
    python blackjack.py
    ```

### 3. Gameplay Rules
1.  You are dealt two cards. The goal is to get as close to **21** as possible without going over.
2.  **[H]it:** Take another card from the deck.
3.  **[S]tand:** Keep your current total and let the dealer play.
4.  **Dealer Rules:** The dealer must continue taking cards until their total is at least 17.

---

## 🧠 Code Structure Highlights

### The Dealer "AI"
The dealer's behavior is controlled by a simple `while` loop. This ensures the dealer always plays consistently and follows the rules of the game.



### Hand Totals
Instead of manually adding every time a card is drawn, we use the `sum()` function on the lists:
```python
player_score = sum(player_hand)
if player_score > 21:
    print("BUST!")

