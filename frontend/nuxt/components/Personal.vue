<template>
  <v-dialog v-model="value" persistent max-width="700px">
    <v-card>
      <v-card-title>
        <!-- <span class="headline">{{$t('headlines.addPlayer')}}</span> -->
        {{personalData}}
      </v-card-title>
      <v-card-text>

      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="grey" flat fab large @click="closeDialog">
          <v-icon>close</v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
import axios from "axios"
export default {
  props: ['value'],
  data() {
    return {
      personalData: {},
    }
  },
  methods: {
    closeDialog() {
      this.$emit('input', false)
    },
  },
  mounted () {
  },
  watch: {
    "value": function () {
      if (this.value) {
        this.personalData = this.$store.state.personalData
      }
    }
  }
}
</script>
