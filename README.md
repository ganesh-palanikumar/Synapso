# Synapso

**Zero-trust. Local-first. Built in the open.**

**Synapso** is a privacy-conscious knowledge system designed to bring **semantic search** to your plain text notes (`.txt`, `.md`)—**without uploading anything anywhere**.

It’s built for people who care about **control, clarity, and clean architecture**.

---

## 🚧 Current Status: Rebuilding from Scratch

Synapso has been rebooted as of version `0.2.0`.

The goal is to build a **fast, minimal, inspectable system** that:
- Runs locally
- Indexes `.txt` and `.md` files
- Embeds them using LLM-powered chunkers
- Stores everything in your local vector store (Qdrant)
- Keeps logs you can read, audit, and trust

No cloud sync. No hidden calls. No black boxes.

---

## 📦 Installation

```bash
pip install synapso

```

## 🧠 Architecture (WIP)

Synapso would be completely local, with zero network chatter. It would use sqlite dbs for both relational and vector storage. The quierying interface would be CLI. Later, I am planning to include a local web GUI and maybe a mac app.

## 🛠 Philosophy

Synapso is meant to be a local-first zero-trust privacy aware interface to query and 'talk' to your knowledge base. As such, it does not make sense to build it behind closed doors. As a result, I am building Synapso in the open. Every line, every commit, every bad decision : it is all out there for anyone to see. 

This is not just a product. It is a journal of how I think as a builder and engineer. 

## 📖 Weekly Devlog

Every Wednesday, I will try to post a new update on [HackerNoon](https://hackernoon.com/u/ganeshpalanikumar) and [Medium](https://medium.com/me/stories/drafts). Stay tuned! The first log is coming up on May 28, 2025!

## 🤝 License & Contributions
- This project is licensed under [Apache 2.0](https://opensource.org/license/apache-2-0)
- The source code is open.
- Contributions are closed - this may change later.
- For now, feel free to explore, fork, or follow along.

## ✉️ Contact
ganesh@synapso.xyz

[Linkedin](https://www.linkedin.com/in/ganesh-palanikumar/)

If you’re into privacy-first tools, semantic search, or just want to see a system built line by line—come along for the ride.
