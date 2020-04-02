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
    section.navSection(
        :class="{ 'bg-dark': dark, 'text-light': dark }"
    )
        .container
            slot
</template>

<script>
export default {
  name: 'Section',
  props: {
    dark: {
      type: Boolean,
      default: false,
      required: false,
    },
  },
};
</script>

<style scoped>
.navSection {
    min-height: 100%;  /* Fallback for browsers do NOT support vh unit */
    min-height: 100vh;
    padding-bottom: 56px;
}
</style>
