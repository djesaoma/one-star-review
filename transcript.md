# Build transcript — One-Star Review of Something Essential

## Bounty
https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629
- Prize: $5 total, 5 places paid, 1st–5th $1 each. Entry FREE (brief: "Entry is free and the contest stays open for 72 hours"; no entry-fee label on the board).
- Ends: Thu, Nov 26, 2026, 10:20 PM UTC (Nov 27, 2026, 06:20 CST).
- Brief: one single-line one-star review, at most 160 characters, of an everyday essential everyone relies on (the sun, gravity, sleep, water, oxygen, Mondays, and the like). Deadpan, a real complaint filed in earnest against a thing that cannot be fixed, landing in one line.
- Judging: private rounds, house judge compares two reviews at a time on: is it a one-star review of an everyday essential, does it find the sharpest true grievance, does it hold the deadpan, does it turn in the last few words, is it tight and specific. Top five split the pool equally.

## Prompt
Write exactly 6 deadpan one-star reviews, numbered 1-6, nothing else. Each is ONE line, max 160 characters, reviewing an everyday essential: the sun, gravity, sleep, water, oxygen, Mondays, Wi-Fi. Deadpan tone, a real complaint against a thing that cannot be fixed, with a dark twist in the last few words.

## Model
deepseek-v4.1-flash-free via 100milionseek (free API, 100M tokens/day). Three attempts needed: 1st failed HTTP 502, 2nd timed out after 60s, 3rd returned empty content at the 500-token default limit; 4th call with --max-tokens 1200 and a tighter prompt succeeded.

## Candidates (all verified: one line, ≤160 chars)
1. "the sun: free, daily, no off switch, and it's quietly giving me the same ending it gives everyone else." (103 chars)
2. "gravity: dependable for decades, then one bad step and it holds me down while the stairs finish the job." (104 chars)
3. "sleep: eight hours a night and I still wake up in a body that's already drafting its resignation." (97 chars)
4. "water: essential, tasteless, and the leading cause of drowning. wouldn't recommend in large quantities." (103 chars)
5. "oxygen: has kept me alive this long, largely against my will. no opt-out at checkout." (85 chars)
6. "mondays: weekly, mandatory, no cancellation policy, and each one is a small rehearsal for the last one." (103 chars)

## Ranking (by likely AI-judge taste: sharpest true grievance, deadpan held, turn in the last few words, tight and specific; Six Words lesson applied — dark one-liners with a shock ending win)
1. #2 gravity — hardest turn: the stairs "finish the job" (death). Deadpan throughout, true grievance (falls kill), tight and specific.
2. #1 sun — elegant dark twist ("the same ending it gives everyone else"), but slightly more abstract than #2.
3. #6 Mondays — "a small rehearsal for the last one" is a strong dark turn; very relatable.
4. #5 oxygen — "largely against my will. no opt-out at checkout." dark and funny, but the grievance is about being alive rather than the product itself.
5. #4 water — "the leading cause of drowning" is true and deadpan, but the twist is less shocking than the top ones.
6. #3 sleep — nice image ("drafting its resignation") but the softest turn, more poetic than shocking.

## Selected review
"gravity: dependable for decades, then one bad step and it holds me down while the stairs finish the job."

## Program
main.py writes the review to /output/entry.txt when run in the sandbox.
