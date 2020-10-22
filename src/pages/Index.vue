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
  Layout(style="position: relative")
    BaseCanvas.fill(style='z-index: 3;' canvasStyle="position: absolute")
      CanvasParticle
    SectionSkills(style="min-height: 80vh; height: 80vh")
    SectionFeed.pt-4.pb-4(style="min-height: 80vh;")
</template>

<script>
import BaseCanvas from '@/components/BaseCanvas';
import CanvasParticle from '@/components/CanvasParticle';
import SectionFeed from "@/components/SectionFeed";
import SectionSkills from "@/components/SectionSkills";

export default {
  name: 'Index',
  components: {
    BaseCanvas,
    CanvasParticle,
    SectionFeed,
    SectionSkills,
  },
  metaInfo: {
    title: "Engineer, Journalist, Entrepreneur"
  },
};
</script>

<page-query>
query {
  allPost {
    totalCount
    edges {
      node {
        id
        title
        timeToRead
        description
        date (format: "MMM D YYYY")
        path
      }
    }
  }
}
</page-query>