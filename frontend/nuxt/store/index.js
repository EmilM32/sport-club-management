import axios from "axios"
export const state = () => ({
  feeData: [],
})
export const actions = {
  async GET_FEE ({ commit }) {
    const { data } = await axios.get('http://localhost:8000/get_data_fee/')
    commit('SET_FEE', data)
  },
}
export const mutations = {
  SET_FEE (state, feeData) {
    state.feeData = feeData
  },
}