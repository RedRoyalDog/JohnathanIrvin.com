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
  b-navbar(toggleable="sm"
      type="dark"
      variant="dark"
      align="center"
      fixed="bottom"
      v-b-scrollspy)
    b-navbar-brand
    b-navbar-toggle(target="nav-collapse")
    b-collapse#nav-collapse(is-nav)
      b-navbar-nav.w-100(fill)
          b-nav-item(href="#home") Home
          b-nav-item(href="#about") About
          b-nav-item(href="#skills") Skills
          b-nav-item(href="#contact") Contact
</template>

<script>
export default {
  name: 'TheNavBar',
};
</script>

<style scoped>
  .bg-dark {
    background-color: #141a20 !important
  }
</style>
