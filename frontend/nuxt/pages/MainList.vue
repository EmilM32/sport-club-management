<template>
  <v-card>
    <div>
      <v-data-table :headers="headers" :items="list" class="text-xs-center">
        <template v-slot:items="props">
          <td>
            <span>{{ props.item.first_name }}</span>
          </td>
          <td>
            <span>{{ props.item.last_name }}</span>
          </td>
          <td>
            <span>{{ props.item.date_of_birth }}</span>
          </td>
          <td>
            <span>{{ props.item.sex }}</span>
          </td>
          <td>
            <span>{{ props.item.level }}</span>
          </td>
          <td>
            <v-btn color="grey" flat fab large @click="personDialog(props.item)">
              <v-icon>person</v-icon>
            </v-btn>
          </td>
        </template>
      </v-data-table>
    </div>
    <AddNewPlayer />
    <Personal v-model="personalDialog" />
  </v-card>
</template>
<script>
import AddNewPlayer from "./../components/AddNewPlayer.vue";
import Personal from "./../components/Personal.vue";
import axios from "axios";
export default {
  components: {
    AddNewPlayer,
    Personal
  },
  data() {
    return {
      dialog: false,
      birthMenu: false,
      personalDialog: false,
      newName: "",
      newSurname: "",
      levelSelected: "",
      gender: ["M", "K"],
      genderSelected: "",
      date: "",
      headers: [
        { text: this.$t("table.name"), value: "first_name", align: "center" },
        { text: this.$t("table.surname"), value: "last_name", align: "center" },
        {
          text: this.$t("table.dateOfBirth"),
          value: "date_of_birth",
          align: "center"
        },
        { text: this.$t("table.sex"), value: "sex", align: "center" },
        { text: this.$t("table.level"), value: "level", align: "center" }
      ],
      level: ["10", "9", "8", "7", "6", "5", "4", "3", "2", "1"],
      list: []
    };
  },
  methods: {
    saveToDb() {
      const dataToSend = {
        name: this.newName,
        surname: this.newSurname,
        birthdate: this.date,
        sex: this.genderSelected,
        level: this.levelSelected
      };
      axios
        .post("http://localhost:8000/send_data_list/", dataToSend)
        .then(response => {})
        .catch(error => {
          console.error("error", error);
        });
      this.dialog = false;
    },
    getData() {
      axios
        .get("http://localhost:8000/get_data_list/")
        .then(response => {
          this.list = response.data.data;
        })
        .catch(error => {
          console.error("error", error);
        });
    },
    personDialog(el) {
      this.personalDialog = true;
      this.$store.commit("PERSONAL_DATA", el);
    }
  },
  mounted() {
    this.getData();
  }
};
</script>