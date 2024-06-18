<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

  <h3 align="center">Gmail-slackbot email summariser</h3>



<!-- ABOUT THE PROJECT -->
## About The Project


This project entails using the Mindsdb tool to make Gmail and Slack databases to then utilise their ML/LLM capabilities in order to make a very capable summarise bot.

Here's why:
* your time is very important and getting a summary of your Emails will allow you to stay productive.
* You shouldn't be losing time on checking your email constantly so automate it with this bot
* You can make this as bespoke as you want this bot is quite brad and accepting of customization

Of course, this bot may not be exactly what you are looking for, but it hopefully becomes a template you change in order to make something amazing that works for you.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Next][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

before running the Jupyter Notebook, I recommend installing Docker Hub. To do so, visit this link
[Docker download](https://docs.docker.com/get-docker/)

### Prerequisites

*Docker for desktop
*Gmail Oauth credentials file
*Slack bot API tokens 
*LLM/ML of your choice API Token

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. have Docker installed
2. Clone the repo
   ```sh
   git clone https://github.com/klorine28/MindsDB_gmail_summariser.git
   ```
3. Install SDK packages
   ```sh
   pip install mindsdb_sdk
   ```
4. run docker comand on the console
   ```js
   docker run --name mindsdb_container -p 47334:47334 -p 47335:47335 mindsdb/mindsdb
   ```
5. open the Jupyter notebook and follow along

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Next.js]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Next-url]: https://www.python.org
[React.js]: https://img.shields.io/badge/Vscode-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white
[React-url]: https://code.visualstudio.com
[Vue.js]: https://cdn.prod.website-files.com/62a8755be8bcc86e6307def8/6329b27b3fc044f886326c4e_mindsDB-full%20logo.svg
[Vue-url]: https://mindsdb.com
[Angular.io]: https://shields.io/badge/MySQL-lightgrey?logo=mysql&style=plastic&logoColor=white&labelColor=blue
[Angular-url]: https://dev.mysql.com/doc/mysql-shell/8.0/en/
[Svelte.dev]: https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white
[Svelte-url]:  https://www.postgresql.org
