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
  div
    canvas(ref="base-canvas" :style="canvasStyle")
    slot
</template>

<script>
export default {
  data: () => {
    return {
      provider: {
        context: null,
        width: null,
        height: null,
      },
    };
  },
  props: ['canvasStyle'],
  provide() {
    return {
      provider: this.provider
    };
  },
  methods: {
      resize() {
        this.provider.width = this.$refs['base-canvas'].parentElement.clientWidth;
        this.provider.height = this.$refs['base-canvas'].parentElement.clientHeight;

        this.$refs['base-canvas'].width = this.provider.width;
        this.$refs['base-canvas'].height = this.provider.height;
      }
  },
  mounted() {
    this.provider.context = this.$refs['base-canvas'].getContext('2d');
    this.resize();

    window.addEventListener('resize', this.resize.bind(this));
  },
};
</script>
