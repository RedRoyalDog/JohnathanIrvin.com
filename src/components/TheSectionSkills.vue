/*
 * Created on Tue Mar 31 2020 by Johnathan Irvin
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

<template lang="pug">
    Section#skills.bg-tan
            h2.text-center.p-2.h1.text-center.d-none Skills
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
                i.devicon-django-plain.colored.icon
                i.devicon-csharp-plain-wordmark.colored.icon
                i.devicon-dot-net-plain-wordmark.colored.icon
                i.devicon-mysql-plain-wordmark.colored.icon
                i.devicon-postgresql-plain-wordmark.colored.icon
                i.devicon-confluence-plain-wordmark.colored.icon
                i.devicon-ssh-plain-wordmark.colored.icon
                i.devicon-devicon-plain-wordmark.icon
                i.devicon-docker-plain-wordmark.colored.icon
                i.devicon-trello-plain-wordmark.colored.icon
                i.devicon-git-plain-wordmark.colored.icon
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
