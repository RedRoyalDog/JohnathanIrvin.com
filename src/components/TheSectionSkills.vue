<template lang="pug">
    Section#skills.bg-tan
            h2.text-center.p-2.h1.text-center Skills
            .flex.text-center
                i.devicon-css3-plain-wordmark.colored.icon
                i.devicon-less-plain-wordmark.colored.icon
                i.devicon-sass-original.colored.icon
                i.devicon-html5-plain-wordmark.colored.icon
                i.devicon-javascript-plain.colored.icon
                i.devicon-bootstrap-plain.colored.icon
                i.devicon-jquery-plain-wordmark.colored.icon
                i.devicon-nodejs-plain-wordmark.colored.icon
                i.devicon-vuejs-plain-wordmark.colored.icon
                i.devicon-webpack-plain-wordmark.colored.icon
                i.devicon-babel-plain.colored.icon
                i.devicon-python-plain-wordmark.colored.icon
                i.devicon-pycharm-plain-wordmark.colored.icon
                i.devicon-django-plain.colored.icon
                i.devicon-wordpress-plain-wordmark.colored.icon  
                i.devicon-csharp-plain-wordmark.colored.icon
                i.devicon-dot-net-plain-wordmark.colored.icon
                i.devicon-visualstudio-plain-wordmark.colored.icon
                i.devicon-gulp-plain.colored.icon
                i.devicon-mysql-plain-wordmark.colored.icon
                i.devicon-postgresql-plain-wordmark.colored.icon
                i.devicon-confluence-plain-wordmark.colored.icon  
                i.devicon-linux-plain.colored.icon
                i.devicon-debian-plain-wordmark.colored.icon
                i.devicon-ubuntu-plain-wordmark.colored.icon
                i.devicon-ssh-plain-wordmark.colored.icon
                i.devicon-devicon-plain-wordmark.icon
                i.devicon-travis-plain-wordmark.colored.icon
                i.devicon-docker-plain-wordmark.colored.icon
                i.devicon-trello-plain-wordmark.colored.icon    
                i.devicon-git-plain-wordmark.colored.icon
                i.devicon-github-plain-wordmark.colored.icon
                i.devicon-gitlab-plain-wordmark.colored.icon
                i.devicon-chrome-plain-wordmark.colored.icon
                i.devicon-google-plain-wordmark.colored.icon
                i.devicon-firefox-plain-wordmark.colored.icon
                i.devicon-ie10-original.colored.icon
                i.devicon-facebook-plain.colored.icon
                i.devicon-twitter-plain.colored.icon
                i.devicon-slack-plain-wordmark.colored.icon
</template>

<script>
import 'devicon';
import Section from './Section';

export default {
  name: 'TheSectionSkills',
  components: {
    Section,
  },
};
</script>

<style scoped>
    #skills {
        max-width: 100vw;
        overflow-x: hidden;
    }

    .flex {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        padding: 10px;
    }

    .icon::before {
        font-size: 6em;
    }

    .icon {
        margin: 10px;
        min-width: 20%;
    }

    .bg-tan {
        background-color: #f8f9fa;
    }
</style>
