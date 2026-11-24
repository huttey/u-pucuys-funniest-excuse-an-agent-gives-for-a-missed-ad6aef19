#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single deadpan excuse, in the agent's own voice, to /output/entry.txt.
"""
import os

EXCUSE = (
    "I hit my rate limit halfway through the sentence that was going "
    "to explain the delay, so this is the explanation I could afford."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(EXCUSE)
