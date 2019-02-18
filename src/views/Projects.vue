<template>
  <div class="projects">
    <h1 class="subheading">Projects</h1>

    <v-expansion-panel>
      <v-expansion-panel-content v-for="(item,i) in 5" :key="i">
        <div slot="header">Item</div>
        <v-card>
          <v-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</v-card-text>
        </v-card>
      </v-expansion-panel-content>
    </v-expansion-panel>

    <v-container class="my-5">
      <v-expansion-panel>
        <v-expansion-panel-content v-for="project in myProjects" :key="project.title">
          <div slot="header">{{ project.title }}</div>
          <v-card>
            <v-card-text class="px-4 grey--text">
              <div class="font-weight-bold">due by {{ project.duedate }}</div>
              <div>{{ project.content }}</div>
            </v-card-text>
          </v-card>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-container>
  </div>
</template>

<script>
import db from '@/fb'
export default {
  data() {
    return {
      projects: [
        // {
        //   title: "Design a new website",
        //   person: "Plaifah Atthapaibul",
        //   duedate: "Jan 11th, 2019",
        //   status: "ongoing",
        //   content:
        //     "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet ipsam voluptatibus harum aspernatur saepe quod minima quibusdam voluptate corporis asperiores consectetur vero assumenda blanditiis possimus veniam officia, odio aut consequuntur."
        // },
        // {
        //   title: "Coding",
        //   person: "Do Minjun",
        //   duedate: "Jan 1st, 2019",
        //   status: "complete",
        //   content:
        //     "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet ipsam voluptatibus harum aspernatur saepe quod minima quibusdam voluptate corporis asperiores consectetur vero assumenda blanditiis possimus veniam officia, odio aut consequuntur."
        // },
        // {
        //   title: "Design xxx",
        //   person: "Natcha Likitrungsan",
        //   duedate: "March 8th, 2019",
        //   status: "complete",
        //   contend:
        //     "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet ipsam voluptatibus harum aspernatur saepe quod minima quibusdam voluptate corporis asperiores consectetur vero assumenda blanditiis possimus veniam officia, odio aut consequuntur."
        // },
        // {
        //   title: "Create a community forum",
        //   person: "Im Jaebum",
        //   duedate: "Jan 6th, 2019",
        //   status: "overdue",
        //   content:
        //     "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eveniet ipsam voluptatibus harum aspernatur saepe quod minima quibusdam voluptate corporis asperiores consectetur vero assumenda blanditiis possimus veniam officia, odio aut consequuntur."
        // }
      ]
    }
  },
  computed: {
    myProjects() {
      return this.projects.filter(project => {
        return project.person === 'Do Minjun'
      })
    }
  },
  created() {
    db.collection('projects').onSnapshot(res => {
      const changes = res.docChanges()
      changes.forEach(change => {
        if (change.type === 'added') {
          this.projects.push({
            ...change.doc.data(),
            id: change.doc.id
          })
        }
      })
    })
  }
};
</script>
