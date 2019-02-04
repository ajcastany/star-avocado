# Star Avocado

---

## Preface

Star Avocado is a simple (and still incomplete) space exploration game featuring an Avocado.

This module sets the basic logic of the first half of the complete game, (still in the works).

Once completed, it will use React instead of the CLI to provide the user interface.

## Usage

Simply run in your terminal `python3 star-avocado.py`

## How to Play

You will find this welcome screen:

[!alt][welcome-screen]

To move around use WASD.  If your terminal does not support getch you will have to press enter after every movement.  Getch is not supported in windows.

Every time you do a movement, you will discover a new location, and a message bellow will appear detailing what's in the just discovered sector.

[!alt][new-sector]

Sometimes you will discover a new planet:

[!alt][new-planet]

To discover the attributes of a Planet you need to scan it with `p`.

[!alt][scan-planet]

You can see a list of all planets, their location and attributes (if the planet has been scanned before)

[!alt][planet-list]

### But be careful!

Some things can harm you, others will heal you.

[!alt][take-damage]

[!alt][heal]

If you run out of Life(🖤) you will die.

[!alt][you-died]

---

[welcome-screen]: /img/welcome-screen.png "Welcome screen"
[new-sector]: /img/new-sector.png "New sector"
[new-planet]: /img/new-planet.png "New Planet"
[scan-planet]: /img/scan-planet.png "Scan Planet"
[planet-list]: /img/planet-list.png "Planet list"
[take-damage]: /img/take-damage.png "Take Damage"
[heal]: /img/heal.png "Healing"
[you-died]: /img/you-died.png "You Died"
