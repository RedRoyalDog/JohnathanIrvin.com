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
    Section#skills.bg-tan(container-classes="align-center")
        h2.text-center.p-2.h1.text-center.d-none Skills
        .flex.text-center
            i.devicon-css3-plain-wordmark.colored.icon
            i.devicon-html5-plain-wordmark.colored.icon
            i.devicon-javascript-plain.colored.icon
            i.devicon-bootstrap-plain.colored.icon
            i.devicon-jquery-plain-wordmark.colored.icon
            i.devicon-nodejs-plain-wordmark.colored.icon
            i.devicon-vuejs-plain-wordmark.colored.icon
            i.devicon-python-plain-wordmark.colored.icon
            i.devicon-csharp-plain-wordmark.colored.icon
            i.devicon-dot-net-plain-wordmark.colored.icon
            i.devicon-confluence-plain-wordmark.colored.icon
            i.devicon-docker-plain-wordmark.colored.icon
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

<style lang="scss">
#skills {
  .align-center {
    display: flex;
    align-items: center;
  }
}
</style>

<style scoped>
    #skills {
        min-height: 100%;
    }

    .flex {
        display: flex;
        align-content: center;
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
