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
    .row.pb-2
      TheSectionAbout.col-md-6
      TheSectionSkills.col-md-6
    .row
      TheSectionContact.col
</template>

<script>
import TheSectionAbout from '../components/TheSectionAbout';
import TheSectionContact from '../components/TheSectionContact';
import TheSectionSkills from '../components/TheSectionSkills';

export default {
  name: 'Home',
  components: {
    TheSectionAbout,
    TheSectionContact,
    TheSectionSkills,
  },
};
</script>
