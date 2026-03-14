# Social Media Content Analytics & Recommendation System

## Overview

This project analyzes social media content performance from Xiaohongshu (RedNote) and Douyin (TikTok China).

The goal is to explore what factors influence engagement in social media posts, including topic, posting time, platform differences, and title keywords.

Using Python-based data analysis, the project identifies patterns in high-performing posts and generates simple recommendations for content strategy.

---

## Motivation

As a content creator interested in data science, I wanted to understand what makes certain posts perform better than others.

Instead of relying on intuition, this project applies data analysis and simple NLP techniques to extract insights from social media content.

---

## Dataset

The dataset contains manually collected social media post data including:

- platform
- title
- topic
- likes
- comments
- posting time

Example:

platform,title,topic,likes,comments,time  
xhs,Study day at university,study,120,15,21  
douyin,Study vlog before finals,study,430,86,20  

---

## Methodology

### Engagement Score

Engagement score is calculated as:

likes + 2 × comments

This approximates the interaction level of a post.

---

### Analysis

The project analyzes:

- engagement by topic
- engagement by platf
