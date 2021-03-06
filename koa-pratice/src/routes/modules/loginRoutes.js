import Router from 'koa-router'
import loginController from '../../api/loginController'

const router = new Router()
router.prefix('/login')
router.post('/forget', loginController.forget)
router.get('/trylogin', loginController.trylogin)
router.post('/login', loginController.login)
router.post('/reg', loginController.reg)

export default router