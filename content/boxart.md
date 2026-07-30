---
title: Boxart & Metadata
group: Games
order: 5
icon: 🖼️
desc: Download cover art and metadata, or set your own.
---

A library full of cover art looks fantastic. Nano can download boxart and game details for your whole collection automatically, and you can also set a cover by hand for any single game.
{: .lead }

![A game list with downloaded boxart](assets/img/shots/xmb_romlist.png)

## The Boxart Scraper

The scraper fetches cover art, background art, and game details (like synopsis, genre, players, and release date) from online databases and caches them on your device.

Open it at **Settings > Game Settings > Boxart Scraper**. From there you can set how scraping works and start a full download.

| Setting | What it does |
|---------|-------------|
| **Scraper service** | Choose the source: **ScreenScraper** (default) or **TheGamesDB**. |
| **Replace Icons with Boxart** | Show downloaded covers in your game lists (default On). |
| **Hover Background Art** | Show fanart behind the highlighted game (default On). |
| **Scrape Region** | Prefer art from a chosen region. |
| **Overwrite Existing** | Re-fetch art you already have (default Off). |
| **ScreenScraper account** | Optional username and password. If left blank, built-in developer credentials are used. |
| **TheGamesDB API key** | Optional key, if you use TheGamesDB. |
| **Scrape All Systems** | Start downloading art and details for your whole library. |

When you choose **Scrape All Systems**, a background thread works through your games during idle time, so you can keep using Nano while it runs. Downloaded art is cached on the device.

You do not need to create an account to scrape from ScreenScraper. The account fields are optional and only speed things up if you have your own login.
{: .callout .tip }

## Per-game boxart

You can also handle a single game on its own. Highlight a game and press the Options button:

| Option | What it does |
|--------|-------------|
| **Scrape This Game** | Re-fetch art and details for just this game (forces an overwrite). |
| **Set Boxart** | Pick any image on your device as this game's cover. |
| **Reset Boxart** | Return to the default icon. Shown only once a custom or scraped cover exists. |
| **Rename / Edit Title** | Change the shown name. This also becomes the search term the scraper uses, so fixing a title can help it find the right art. |
| **Information** | See the full details page: cover, fanart, synopsis, genre, players, rating, date, developer, publisher, and file path and size. |

If the scraper cannot find the right cover for a game, try **Rename / Edit Title** to correct the name first, then **Scrape This Game** again.
{: .callout .note }

## Per-system scraping

You can also scrape one system at a time from the **Game Systems** editor. Each system has a **Scrape This System** action, plus optional scraper account fields to override the global setting for just that system. See [Game Systems](game-systems.html).

## Related pages

- [Game Systems](game-systems.html) for per-system scraper settings.
- [Context Menus](context-menus.html) for every Options-menu action on a game.
- [Collections & Recently Played](collections.html) for grouping your games.
