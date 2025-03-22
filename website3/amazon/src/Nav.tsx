import './static/Nav.css'
import logo from './assets/logo.png'

function Nav() {
  return (
    <nav className='flex bg-[#0f1111]'>
        
        <div className="item"><img src={logo} className='h-10 w-36' alt="" /></div>
        <div className='flex flex-col justify-start'>
            <span className='text-slate-100 text-[12px]'>&nbsp;&nbsp;Delivering to Surat 395 007</span>
            <span className='text-white font-bold text-[14px]'>Update location</span>
        </div>
        
    </nav>
  )
}

export default Nav
