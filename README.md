# GitHub AutoScraper + Change Alerts

Using GitHub Actions and Python, this repo automatically scrapes the content of the BBC's homepage every four hours and sends the content to me as an attachment in my email **if it has been changed**. You'll want to update the repository secrets with a `SENDGRID_API_KEY`, `TO_EMAIL` and `FROM_EMAIL`.

A tiny combo of [autoscraper-mailer](https://github.com/jsoma/autoscraper-history) and [autoscraper-history](https://github.com/jsoma/autoscraper-history), which are in turn a simple Python-driven example of @simonw's [Git Scraping](https://simonwillison.net/2020/Oct/9/git-scraping/).