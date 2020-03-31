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
    Section#contact.flex: b-container
        h2.text-center.h1 Contact
        FormContact
</template>

<script>
import Section from './Section';
import FormContact from './FormContact';

export default {
  name: 'TheSectionContact',
  components: {
    Section,
    FormContact,
  },
};
</script>

<style scoped>
    .flex {
        display: flex;
        align-items: center;
        justify-content: center;
    }
</style>
