from helpers.display import divider_line

def pause():
    """Pause the program until the user presses Enter."""
    input("\nPress Enter to continue...")


def granny_square_pattern():
    """Display a generic pattern for a granny square using a magic ring."""
    print(
        "Simple Granny Square Pattern (Magic Ring Version)")
    divider_line()
    print(
        """Round 1:
        - Make a magic ring. (or chain 4, join with slip stitch to form a ring)
        - Ch 3 (counts as dc), then work 2 dc into the ring.
        - *Ch 2, 3 dc into the ring* — repeat 3 more times.
        - Ch 2 and pull the ring closed.
        - Join with a sl st to the top of the beginning ch-3.
        
        Round 2:
        - Sl st into the next ch-2 corner space.
        - Ch 3, 2 dc, ch 2, 3 dc in the same corner.
        - In each remaining corner: 3 dc, ch 2, 3 dc.
        - Join with a sl st.
        
        Round 3 and Beyond:
        - In each corner: 3 dc, ch 2, 3 dc.
        - In each side space: 3 dc.
        - Join with a sl st at the end of each round.
        
        Continue until your square is the size you want!"""
    )


def blanket_instructions():
    """Displays the instructions for making the temperature blanket using this app."""
    divider_line()
    print("\nTemperature Blanket Instructions (12‑Square Version)")
    divider_line()
    print(
        """This project uses one large granny square for each month of the year.
How it works:
    - You will make 12 squares total — one for each month.
    - Each day of the month adds ONE round to that month's square.
    - Day 1 has TWO rounds:
        • the center round (Round 1)
        • the temperature round for Day 1
    - By the end of the month, your square will have 29–32 rounds
      depending on how many days are in that month
    - Each round's color is based on that day's high temperature.
As you finish each month, you can join the squares right away or 
you can wait until the end of the year.  Either way works!"
        
When the year is complete, you'll have 12 beautiful squares that
show the temperature story of your entire year."""
    )