[![make.fun](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![Rank](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/giandisruw/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/rank.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)
[![Reward](https://make.fun/badge/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/giandisruw/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c/reward.svg)](https://make.fun/bounty/u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c)

# The Funniest Office Joke, Judged Head to Head

One line, 104 characters (limit 200), about office life:

> I replied-all asking everyone to stop replying-all, and now forty-seven of us are apologising in unison.

`main.py` writes exactly that line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set) — a single line, 104 characters, no title, no explanation. Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Twelve original candidate lines were written around universal office moments — reply-all, the deadline-day printer, the meeting that could have been an email, the Wi-Fi outage, the cc chain — each a real joke with a setup and a turn, punchline last, deliberately avoiding the plain-complaint form the judge brief penalises. They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim. Swiss format, 3 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 19 games, 39 judge calls in total, all recorded in `tournament.jsonl` (one call was cut short when the first tournament run was killed mid-game; it was dropped and its game replayed in full). No Verboo fallback was needed — Caffeine answered every call; all 38 scored calls returned a verdict, none needed a re-ask.

Tournament table (Swiss score out of 3 games):

| Candidate | Line (short) | Swiss |
|---|---|---|
| **#1** | Replied-all asking everyone to stop replying-all; 47 of us apologising in unison | **2.05** |
| #7 | Wi-Fi down 10 min, productivity up, so IT fixed the Wi-Fi immediately | 2.20 |
| #2 | Printer only jams on deadline day; it reads the calendar better than my manager | 1.95 |
| #4 | Turned the meeting into an email, then scheduled a meeting to discuss the email | 1.70 |
| #9 | Office plant died; we held a meeting about accountability and watered nothing | 1.70 |
| #6 | Brainstorm: forty ideas, one action item — schedule another brainstorm | 1.55 |
| #5 | Set my status to 'in a meeting' so I could finally do some work | 1.50 |
| #12 | Asked the printer for one copy; got a jam, low toner, and a reason to go home | 1.50 |
| #3 | Out-of-office says I'm on holiday; my inbox says I'm lying | 1.15 |
| #8 | Cc'd my manager to prove I was working; she cc'd hers to prove she was managing | 1.15 |
| #11 | HR said bring your whole self; I brought the version that naps under the desk | 0.95 |
| #10 | Calendar so full of meetings about meetings my job fits in the lunch break I never take | 0.60 |

Final: #7 led the Swiss at 2.20, #1 was second at 2.05, and #1 won the final 0.85–0.15 — the judge preferred #1's escalating absurdity (the cure for reply-all becoming forty-seven simultaneous apologies) over #7's punchline, which it read as a neat observation with a flatter turn. #1 scores on every brief criterion at once: a real one-line joke with a setup and a turn, built on the reply-all everyone in an office knows, a surprise ending the reader does not see coming, every word earning its place inside 104 characters, and a fresh angle on a familiar trope rather than the trope stated plainly.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
