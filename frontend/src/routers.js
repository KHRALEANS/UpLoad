import {createRouter, createWebHistory} from 'vue-router'
import Home from './components/Home'
import Student from './components/Student'
import Teacher from './components/Teacher'



const routes = [
    {
        path:'/student',
        name:'student',
        component:Student
    },

    {
        path:'/teacher',
        name:'teacher',
        component:Teacher
    },

    {
        path:'/',
        name:'home',
        component:Home
    },
]


const router = createRouter({
    history:createWebHistory(),
    routes
})


export default router;
