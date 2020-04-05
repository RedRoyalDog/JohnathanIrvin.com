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
    Section#about(container-classes="align-center")
      BaseCanvas.fill(style='z-index: 3')
        CanvasParticle
      .container.content
        h1.h1.pb-2 Johnathan Irvin
        p: VueTyper(:text='what' caret-animation='blink')
      p.bottom-center: i.down
</template>

<script>
import BaseCanvas from '../components/BaseCanvas';
import CanvasParticle from '../components/CanvasParticle';
import Section from './Section';
import { VueTyper } from 'vue-typer'

export default {
  name: 'TheSectionAbout',
  components: {
    BaseCanvas,
    CanvasParticle,
    Section,
    VueTyper
  },
  data: function() {
    return {
      what: ['Senior Software Engineer', 'Journalist', 'Entrepreneur', 'Creator', 'Inventor'],
    }
  },
};
</script>

<style lang="scss">
#about {
  .align-center {
    display: flex;
    align-items: center;
  }
}
</style>

<style lang="scss" scoped>
#about {
  background-color: black;
  position: relative;
  z-index: 2;

  .container, p, h1 {
    position: relative;
    z-index: 5;
  }

  p, h1 {
    color: #33FF33;
    font-family: monospace;
    -webkit-animation: glow 1s ease-in-out infinite alternate;
    -moz-animation: glow 1s ease-in-out infinite alternate;
    animation: glow 1s ease-in-out infinite alternate;
  }

  p {
    font-size: 1.5rem;
    font-weight: 400;
    line-height: 1.5;
  }
}

#about::after {
  content: "";
  background: url(../assets/img1.jpg) no-repeat center center;
  background-size: cover;
  background-attachment: fixed;
  opacity: 0.39;

  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  position: absolute;
  z-index: 1;
}

.fill {
  position: absolute;
  width: 100%;
  height: 100%;

  top: 0;
  left: 0;
}
</style>

<style lang="scss">
.vue-typer {
  font-family: monospace;

  .custom.char {
    /* https://superuser.com/questions/361297/what-colour-is-the-dark-green-on-old-fashioned-green-screen-computer-displays */
    color: #33FF33;

    -webkit-animation: glow 1s ease-in-out infinite alternate;
    -moz-animation: glow 1s ease-in-out infinite alternate;
    animation: glow 1s ease-in-out infinite alternate;
  }

  .custom.caret {
    background-color: #33FF33;
  }
}

@-webkit-keyframes glow {
  from {
    text-shadow: 0 0 .5px #000, 0 0 .5px #000, 0 0 .5px #33FF33, 0 0 .5px #33FF33, 0 0 .5px #33FF33, 0 0 .5px #33FF33, 0 0 .5px #33FF33;
  }
  to {
    text-shadow: 0 0 1px #000, 0 0 1px #33FF33, 0 0 1px #33FF33, 0 0 1px #33FF33, 0 0 1px #33FF33, 0 0 1px #33FF33, 0 0 1px #33FF33;
  }
}

.bottom-center {
  position: absolute !important;
  bottom: 0;
  right: 10%;
}

.down {
  width: 10px;
  height: 10px;
  color: white;
  border: solid;
  border-top: none;
  border-left: none;
  display: inline-block;
  position: relative;
  transform: rotate(45deg);
  -webkit-transform: rotate(45deg);

  animation-name: bounce;
  animation-duration: 2s;
  animation-iteration-count: infinite;
}

@keyframes bounce {
  0%   {top: -5px}
  50%  {top: 5px}
  100% {top: -5px}
}
</style>