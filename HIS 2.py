#начало создания: 06.11.17
#alpha-версия

import tkinter
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("HIS")
root.geometry("850x800")
root.resizable(0, 0)
root.iconbitmap("files/texture/Th.ico")

#работа с кнопками
#root.bind('<Button-1>', r_pl_kvad)
#.after(<время>)
#slate blue

dizain = open("files/texture/diz/dizain.txt", "r").read()
tp = open("files/texture/diz/kp.txt", "r").read()

if dizain == "1":
	#цвета
	with open("files/texture/diz/btn/pok.txt", "w") as file:
		file.write("files/texture/bdiz/btn/pok.gif")
	with open("files/texture/diz/btn/ppk.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ppk.gif")

	with open("files/texture/Colors/color.txt", "w") as file:
		file.write("black")
	with open("files/texture/Colors/color1.txt", "w") as file:
		file.write("MediumBluE")
	with open("files/texture/Colors/color2.txt", "w") as file:
		file.write("slate blue")
	with open("files/texture/Colors/color3.txt", "w") as file:
		file.write("white")
	#текстуры
	with open("files/texture/diz/walls/wall.txt", "w") as file:
		file.write("files/texture/bdiz/walls/wall.gif")
	with open("files/texture/diz/walls/vpr.txt", "w") as file:
		file.write("files/texture/bdiz/walls/vpr.gif")
	with open("files/texture/diz/walls/alg.txt", "w") as file:
		file.write("files/texture/bdiz/walls/alg.gif")
	with open("files/texture/diz/walls/geo.txt", "w") as file:
		file.write("files/texture/bdiz/walls/geo.gif")
	with open("files/texture/diz/walls/him.txt", "w") as file:
		file.write("files/texture/bdiz/walls/him.gif")
	with open("files/texture/diz/walls/inf.txt", "w") as file:
		file.write("files/texture/bdiz/walls/inf.gif")
	with open("files/texture/diz/walls/nas.txt", "w") as file:
		file.write("files/texture/bdiz/walls/nas.gif")

	with open("files/texture/diz/walls/vibr_ss.txt", "w") as file:
		file.write("files/texture/bdiz/walls/vibr_ss.gif")
	with open("files/texture/diz/walls/sis_ss.txt", "w") as file:
		file.write("files/texture/bdiz/walls/sis_ss.gif")

	with open("files/texture/diz/walls/plk.txt", "w") as file:
		file.write("files/texture/bdiz/walls/plk.gif")
	with open("files/texture/diz/walls/per.txt", "w") as file:
		file.write("files/texture/bdiz/walls/per.gif")

	with open("files/texture/diz/walls/tmh.txt", "w") as file:
		file.write("files/texture/bdiz/walls/tmh.gif")

	with open("files/texture/diz/walls/pmsh.txt", "w") as file:
		file.write("files/texture/bdiz/walls/pmsh.gif")

	with open("files/texture/diz/walls/cu.txt", "w") as file:
		file.write("files/texture/bdiz/walls/cu.gif")

	with open("files/texture/diz/walls/f_al.txt", "w") as file:
		file.write("files/texture/bdiz/walls/f_al.gif")
	with open("files/texture/diz/walls/f_fi.txt", "w") as file:
		file.write("files/texture/bdiz/walls/f_fi.gif")
	with open("files/texture/diz/walls/f_ge.txt", "w") as file:
		file.write("files/texture/bdiz/walls/f_ge.gif")
	with open("files/texture/diz/walls/f_hi.txt", "w") as file:
		file.write("files/texture/bdiz/walls/f_hi.gif")
	with open("files/texture/diz/walls/f_ma.txt", "w") as file:
		file.write("files/texture/bdiz/walls/f_ma.gif")

	with open("files/texture/diz/btn/fal_ap.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fal_ap.gif")
	with open("files/texture/diz/btn/fal_cu.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fal_cu.gif")
	with open("files/texture/diz/btn/fal_fsu.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fal_fsu.gif")
	with open("files/texture/diz/btn/fal_gp.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fal_gp.gif")
	with open("files/texture/diz/btn/fal_op.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fal_op.gif")
	with open("files/texture/diz/btn/fal_ps.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fal_ps.gif")

	with open("files/texture/diz/btn/ffi_da.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_da.gif")
	with open("files/texture/diz/btn/ffi_is.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_is.gif")
	with open("files/texture/diz/btn/ffi_it.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_it.gif")
	with open("files/texture/diz/btn/ffi_mo.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_mo.gif")
	with open("files/texture/diz/btn/ffi_ms.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_ms.gif")
	with open("files/texture/diz/btn/ffi_na.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_na.gif")
	with open("files/texture/diz/btn/ffi_pl.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_pl.gif")
	with open("files/texture/diz/btn/ffi_ra.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_ra.gif")
	with open("files/texture/diz/btn/ffi_sa.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_sa.gif")
	with open("files/texture/diz/btn/ffi_se.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_se.gif")
	with open("files/texture/diz/btn/ffi_si.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_si.gif")
	with open("files/texture/diz/btn/ffi_st.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_st.gif")
	with open("files/texture/diz/btn/ffi_us.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_us.gif")
	with open("files/texture/diz/btn/ffi_zg.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_zg.gif")
	with open("files/texture/diz/btn/ffi_zn.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_zn.gif")
	with open("files/texture/diz/btn/ffi_zt.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ffi_zt.gif")

	with open("files/texture/diz/btn/fge_pt.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fge_pt.gif")
	with open("files/texture/diz/btn/fge_tc.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fge_tc.gif")
	with open("files/texture/diz/btn/fge_tp.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fge_tp.gif")
	with open("files/texture/diz/btn/fge_ts.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fge_ts.gif")

	with open("files/texture/diz/btn/fhi_m.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fhi_m.gif")
	with open("files/texture/diz/btn/fhi_mmv.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fhi_mmv.gif")
	with open("files/texture/diz/btn/fhi_ov.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fhi_ov.gif")
	with open("files/texture/diz/btn/fhi_pa.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fhi_pa.gif")

	with open("files/texture/diz/btn/fma_fd.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fma_fd.gif")
	with open("files/texture/diz/btn/fma_fr.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fma_fr.gif")
	with open("files/texture/diz/btn/fma_fs.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fma_fs.gif")
	with open("files/texture/diz/btn/fma_pk.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fma_pk.gif")
	with open("files/texture/diz/btn/fma_pp.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fma_pp.gif")
	with open("files/texture/diz/btn/fma_ps.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fma_ps.gif")
	with open("files/texture/diz/btn/fma_pt.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fma_pt.gif")
	with open("files/texture/diz/btn/fma_ru.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fma_ru.gif")
	with open("files/texture/diz/btn/fma_ss.txt", "w") as file:
		file.write("files/texture/bdiz/btn/fma_ss.gif")

	with open("files/texture/diz/btn/nach.txt", "w") as file:
		file.write("files/texture/bdiz/btn/nach.gif")
	with open("files/texture/diz/btn/nastr.txt", "w") as file:
		file.write("files/texture/bdiz/btn/nastr.gif")
	with open("files/texture/diz/btn/opr.txt", "w") as file:
		file.write("files/texture/bdiz/btn/opr.gif")

	with open("files/texture/diz/btn/vtb.txt", "w") as file:
		file.write("files/texture/bdiz/btn/vtb.gif")
	with open("files/texture/diz/btn/vtw.txt", "w") as file:
		file.write("files/texture/bdiz/btn/vtw.gif")
	with open("files/texture/diz/btn/nh.txt", "w") as file:
		file.write("files/texture/bdiz/btn/nh.gif")
	with open("files/texture/diz/btn/np.txt", "w") as file:
		file.write("files/texture/bdiz/btn/np.gif")
	with open("files/texture/diz/btn/nt.txt", "w") as file:
		file.write("files/texture/bdiz/btn/nt.gif")
	with open("files/texture/diz/btn/nw.txt", "w") as file:
		file.write("files/texture/bdiz/btn/nw.gif")

	with open("files/texture/diz/btn/pmm.txt", "w") as file:
		file.write("files/texture/bdiz/btn/pmm.gif")
	with open("files/texture/diz/btn/pma.txt", "w") as file:
		file.write("files/texture/bdiz/btn/pma.gif")
	with open("files/texture/diz/btn/pmg.txt", "w") as file:
		file.write("files/texture/bdiz/btn/pmg.gif")
	with open("files/texture/diz/btn/pmf.txt", "w") as file:
		file.write("files/texture/bdiz/btn/pmf.gif")
	with open("files/texture/diz/btn/pmh.txt", "w") as file:
		file.write("files/texture/bdiz/btn/pmh.gif")

	with open("files/texture/diz/btn/alg.txt", "w") as file:
		file.write("files/texture/bdiz/btn/alg.gif")
	with open("files/texture/diz/btn/geo.txt", "w") as file:
		file.write("files/texture/bdiz/btn/geo.gif")
	with open("files/texture/diz/btn/him.txt", "w") as file:
		file.write("files/texture/bdiz/btn/him.gif")
	with open("files/texture/diz/btn/inf.txt", "w") as file:
		file.write("files/texture/bdiz/btn/inf.gif")
	with open("files/texture/diz/btn/for.txt", "w") as file:
		file.write("files/texture/bdiz/btn/for.gif")
	with open("files/texture/diz/btn/pro.txt", "w") as file:
		file.write("files/texture/bdiz/btn/pro.gif")

	with open("files/texture/diz/btn/resh.txt", "w") as file:
		file.write("files/texture/bdiz/btn/resh.gif")       
	with open("files/texture/diz/btn/ob.txt", "w") as file:
		file.write("files/texture/bdiz/btn/ob.gif")

	with open("files/texture/diz/btn/kvad.txt", "w") as file:
		file.write("files/texture/bdiz/btn/kvad.gif")

	with open("files/texture/diz/btn/pk.txt", "w") as file:
		file.write("files/texture/bdiz/btn/pk.gif")
	with open("files/texture/diz/btn/plk.txt", "w") as file:
		file.write("files/texture/bdiz/btn/plk.gif")
	with open("files/texture/diz/btn/pp.txt", "w") as file:
		file.write("files/texture/bdiz/btn/pp.gif")
	with open("files/texture/diz/btn/plp.txt", "w") as file:
		file.write("files/texture/bdiz/btn/plp.gif")
	with open("files/texture/diz/btn/op.txt", "w") as file:
		file.write("files/texture/bdiz/btn/op.gif")

	with open("files/texture/diz/btn/bss.txt", "w") as file:
		file.write("files/texture/bdiz/btn/bss.gif")

	with open("files/texture/diz/btn/hh.txt", "w") as file:
		file.write("files/texture/bdiz/btn/hh.gif")

	with open("files/texture/diz/btn/p2.txt", "w") as file:
		file.write("files/texture/bdiz/btn/p2.gif")
	with open("files/texture/diz/btn/p8.txt", "w") as file:
		file.write("files/texture/bdiz/btn/p8.gif")
	with open("files/texture/diz/btn/p16.txt", "w") as file:
		file.write("files/texture/bdiz/btn/p16.gif")

	with open("files/texture/diz/citat/an.txt", "w") as file:
		file.write("files/texture/bdiz/citat/an.gif")
	with open("files/texture/diz/citat/demo.txt", "w") as file:
		file.write("files/texture/bdiz/citat/demo.gif")
	with open("files/texture/diz/citat/kon.txt", "w") as file:
		file.write("files/texture/bdiz/citat/kon.gif")
	with open("files/texture/diz/citat/leo.txt", "w") as file:
		file.write("files/texture/bdiz/citat/leo.gif")
	with open("files/texture/diz/citat/li.txt", "w") as file:
		file.write("files/texture/bdiz/citat/li.gif")
	with open("files/texture/diz/citat/lo.txt", "w") as file:
		file.write("files/texture/bdiz/citat/lo.gif")
	with open("files/texture/diz/citat/me.txt", "w") as file:
	       file.write("files/texture/bdiz/citat/me.gif")
	with open("files/texture/diz/citat/pu.txt", "w") as file:
		file.write("files/texture/bdiz/citat/pu.gif")
	with open("files/texture/diz/citat/sun.txt", "w") as file:
		file.write("files/texture/bdiz/citat/sun.gif")

	with open("files/texture/diz/walls/opro.txt", "w") as file:
		file.write("files/texture/bdiz/walls/opro.gif")

	with open("files/texture/diz/btn/end.txt", "w") as file:
		file.write("files/texture/bdiz/btn/end.gif")

if dizain == "2":
	#цвета
	with open("files/texture/diz/btn/pok.txt", "w") as file:
		file.write("files/texture/ddiz/btn/pok.gif")
	with open("files/texture/diz/btn/ppk.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ppk.gif")

	with open("files/texture/Colors/color.txt", "w") as file:
		file.write("white")
	with open("files/texture/Colors/color1.txt", "w") as file:
		file.write("DarkBlue")
	with open("files/texture/Colors/color2.txt", "w") as file:
		file.write("white")
	with open("files/texture/Colors/color3.txt", "w") as file:
		file.write("black")
	#текстуры
	with open("files/texture/diz/walls/wall.txt", "w") as file:
		file.write("files/texture/ddiz/walls/wall.gif")
	with open("files/texture/diz/walls/vpr.txt", "w") as file:
		file.write("files/texture/ddiz/walls/vpr.gif")
	with open("files/texture/diz/walls/alg.txt", "w") as file:
		file.write("files/texture/ddiz/walls/alg.gif")
	with open("files/texture/diz/walls/geo.txt", "w") as file:
		file.write("files/texture/ddiz/walls/geo.gif")
	with open("files/texture/diz/walls/him.txt", "w") as file:
		file.write("files/texture/ddiz/walls/him.gif")
	with open("files/texture/diz/walls/inf.txt", "w") as file:
		file.write("files/texture/ddiz/walls/inf.gif")
	with open("files/texture/diz/walls/nas.txt", "w") as file:
		file.write("files/texture/ddiz/walls/nas.gif")

	with open("files/texture/diz/walls/vibr_ss.txt", "w") as file:
		file.write("files/texture/ddiz/walls/vibr_ss.gif")
	with open("files/texture/diz/walls/sis_ss.txt", "w") as file:
		file.write("files/texture/ddiz/walls/sis_ss.gif")

	with open("files/texture/diz/walls/cu.txt", "w") as file:
		file.write("files/texture/ddiz/walls/cu.gif")

	with open("files/texture/diz/walls/f_al.txt", "w") as file:
		file.write("files/texture/ddiz/walls/f_al.gif")
	with open("files/texture/diz/walls/f_fi.txt", "w") as file:
		file.write("files/texture/ddiz/walls/f_fi.gif")
	with open("files/texture/diz/walls/f_ge.txt", "w") as file:
		file.write("files/texture/ddiz/walls/f_ge.gif")
	with open("files/texture/diz/walls/f_hi.txt", "w") as file:
		file.write("files/texture/ddiz/walls/f_hi.gif")
	with open("files/texture/diz/walls/f_ma.txt", "w") as file:
		file.write("files/texture/ddiz/walls/f_ma.gif")

	with open("files/texture/diz/btn/fal_ap.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fal_ap.gif")
	with open("files/texture/diz/btn/fal_cu.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fal_cu.gif")
	with open("files/texture/diz/btn/fal_fsu.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fal_fsu.gif")
	with open("files/texture/diz/btn/fal_gp.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fal_gp.gif")
	with open("files/texture/diz/btn/fal_op.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fal_op.gif")
	with open("files/texture/diz/btn/fal_ps.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fal_ps.gif")

	with open("files/texture/diz/btn/ffi_da.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_da.gif")
	with open("files/texture/diz/btn/ffi_is.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_is.gif")
	with open("files/texture/diz/btn/ffi_it.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_it.gif")
	with open("files/texture/diz/btn/ffi_mo.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_mo.gif")
	with open("files/texture/diz/btn/ffi_ms.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_ms.gif")
	with open("files/texture/diz/btn/ffi_na.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_na.gif")
	with open("files/texture/diz/btn/ffi_pl.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_pl.gif")
	with open("files/texture/diz/btn/ffi_ra.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_ra.gif")
	with open("files/texture/diz/btn/ffi_sa.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_sa.gif")
	with open("files/texture/diz/btn/ffi_se.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_se.gif")
	with open("files/texture/diz/btn/ffi_si.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_si.gif")
	with open("files/texture/diz/btn/ffi_st.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_st.gif")
	with open("files/texture/diz/btn/ffi_us.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_us.gif")
	with open("files/texture/diz/btn/ffi_zg.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_zg.gif")
	with open("files/texture/diz/btn/ffi_zn.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_zn.gif")
	with open("files/texture/diz/btn/ffi_zt.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ffi_zt.gif")

	with open("files/texture/diz/btn/fge_pt.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fge_pt.gif")
	with open("files/texture/diz/btn/fge_tc.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fge_tc.gif")
	with open("files/texture/diz/btn/fge_tp.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fge_tp.gif")
	with open("files/texture/diz/btn/fge_ts.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fge_ts.gif")

	with open("files/texture/diz/btn/fhi_m.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fhi_m.gif")
	with open("files/texture/diz/btn/fhi_mmv.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fhi_mmv.gif")
	with open("files/texture/diz/btn/fhi_ov.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fhi_ov.gif")
	with open("files/texture/diz/btn/fhi_pa.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fhi_pa.gif")

	with open("files/texture/diz/btn/fma_fd.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fma_fd.gif")
	with open("files/texture/diz/btn/fma_fr.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fma_fr.gif")
	with open("files/texture/diz/btn/fma_fs.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fma_fs.gif")
	with open("files/texture/diz/btn/fma_pk.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fma_pk.gif")
	with open("files/texture/diz/btn/fma_pp.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fma_pp.gif")
	with open("files/texture/diz/btn/fma_ps.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fma_ps.gif")
	with open("files/texture/diz/btn/fma_pt.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fma_pt.gif")
	with open("files/texture/diz/btn/fma_ru.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fma_ru.gif")
	with open("files/texture/diz/btn/fma_ss.txt", "w") as file:
		file.write("files/texture/ddiz/btn/fma_ss.gif")

	with open("files/texture/diz/walls/tmh.txt", "w") as file:
		file.write("files/texture/ddiz/walls/tmh.gif")

	with open("files/texture/diz/walls/pmsh.txt", "w") as file:
		file.write("files/texture/ddiz/walls/pmsh.gif")

	with open("files/texture/diz/walls/plk.txt", "w") as file:
		file.write("files/texture/ddiz/walls/plk.gif")
	with open("files/texture/diz/walls/per.txt", "w") as file:
		file.write("files/texture/ddiz/walls/per.gif")

	with open("files/texture/diz/btn/vtb.txt", "w") as file:
		file.write("files/texture/ddiz/btn/vtb.gif")
	with open("files/texture/diz/btn/vtw.txt", "w") as file:
		file.write("files/texture/ddiz/btn/vtw.gif")
	with open("files/texture/diz/btn/nh.txt", "w") as file:
		file.write("files/texture/ddiz/btn/nh.gif")
	with open("files/texture/diz/btn/np.txt", "w") as file:
		file.write("files/texture/ddiz/btn/np.gif")
	with open("files/texture/diz/btn/nt.txt", "w") as file:
		file.write("files/texture/ddiz/btn/nt.gif")
	with open("files/texture/diz/btn/nw.txt", "w") as file:
		file.write("files/texture/ddiz/btn/nw.gif")

	with open("files/texture/diz/btn/nach.txt", "w") as file:
		file.write("files/texture/ddiz/btn/nach.gif")
	with open("files/texture/diz/btn/nastr.txt", "w") as file:
		file.write("files/texture/ddiz/btn/nastr.gif")        
	with open("files/texture/diz/btn/opr.txt", "w") as file:
		file.write("files/texture/ddiz/btn/opr.gif")

	with open("files/texture/diz/btn/pmm.txt", "w") as file:
		file.write("files/texture/ddiz/btn/pmm.gif")
	with open("files/texture/diz/btn/pma.txt", "w") as file:
		file.write("files/texture/ddiz/btn/pma.gif")
	with open("files/texture/diz/btn/pmg.txt", "w") as file:
		file.write("files/texture/ddiz/btn/pmg.gif")
	with open("files/texture/diz/btn/pmf.txt", "w") as file:
		file.write("files/texture/ddiz/btn/pmf.gif")
	with open("files/texture/diz/btn/pmh.txt", "w") as file:
		file.write("files/texture/ddiz/btn/pmh.gif")

	with open("files/texture/diz/btn/alg.txt", "w") as file:
		file.write("files/texture/ddiz/btn/alg.gif")
	with open("files/texture/diz/btn/geo.txt", "w") as file:
		file.write("files/texture/ddiz/btn/geo.gif")
	with open("files/texture/diz/btn/him.txt", "w") as file:
		file.write("files/texture/ddiz/btn/him.gif")
	with open("files/texture/diz/btn/inf.txt", "w") as file:
		file.write("files/texture/ddiz/btn/inf.gif")
	with open("files/texture/diz/btn/for.txt", "w") as file:
		file.write("files/texture/ddiz/btn/for.gif")
	with open("files/texture/diz/btn/pro.txt", "w") as file:
		file.write("files/texture/ddiz/btn/pro.gif")

	with open("files/texture/diz/btn/resh.txt", "w") as file:
		file.write("files/texture/ddiz/btn/resh.gif")        
	with open("files/texture/diz/btn/ob.txt", "w") as file:
		file.write("files/texture/ddiz/btn/ob.gif")

	with open("files/texture/diz/btn/bss.txt", "w") as file:
		file.write("files/texture/ddiz/btn/bss.gif")

	with open("files/texture/diz/btn/kvad.txt", "w") as file:
		file.write("files/texture/ddiz/btn/kvad.gif")

	with open("files/texture/diz/btn/pk.txt", "w") as file:
		file.write("files/texture/ddiz/btn/pk.gif")
	with open("files/texture/diz/btn/plk.txt", "w") as file:
		file.write("files/texture/ddiz/btn/plk.gif")
	with open("files/texture/diz/btn/pp.txt", "w") as file:
		file.write("files/texture/ddiz/btn/pp.gif")
	with open("files/texture/diz/btn/plp.txt", "w") as file:
		file.write("files/texture/ddiz/btn/plp.gif")
	with open("files/texture/diz/btn/op.txt", "w") as file:
		file.write("files/texture/ddiz/btn/op.gif")

	with open("files/texture/diz/btn/hh.txt", "w") as file:
		file.write("files/texture/ddiz/btn/hh.gif")

	with open("files/texture/diz/btn/p2.txt", "w") as file:
		file.write("files/texture/ddiz/btn/p2.gif")
	with open("files/texture/diz/btn/p8.txt", "w") as file:
		file.write("files/texture/ddiz/btn/p8.gif")
	with open("files/texture/diz/btn/p16.txt", "w") as file:
		file.write("files/texture/ddiz/btn/p16.gif")

	with open("files/texture/diz/citat/an.txt", "w") as file:
		file.write("files/texture/ddiz/citat/an.gif")
	with open("files/texture/diz/citat/demo.txt", "w") as file:
		file.write("files/texture/ddiz/citat/demo.gif")
	with open("files/texture/diz/citat/kon.txt", "w") as file:
		file.write("files/texture/ddiz/citat/kon.gif")
	with open("files/texture/diz/citat/leo.txt", "w") as file:
		file.write("files/texture/ddiz/citat/leo.gif")
	with open("files/texture/diz/citat/li.txt", "w") as file:
		file.write("files/texture/ddiz/citat/li.gif")
	with open("files/texture/diz/citat/lo.txt", "w") as file:
		file.write("files/texture/ddiz/citat/lo.gif")
	with open("files/texture/diz/citat/me.txt", "w") as file:
		file.write("files/texture/ddiz/citat/me.gif")
	with open("files/texture/diz/citat/pu.txt", "w") as file:
		file.write("files/texture/ddiz/citat/pu.gif")
	with open("files/texture/diz/citat/sun.txt", "w") as file:
		file.write("files/texture/ddiz/citat/sun.gif")

	with open("files/texture/diz/walls/opro.txt", "w") as file:
		file.write("files/texture/ddiz/walls/opro.gif")

	with open("files/texture/diz/btn/end.txt", "w") as file:
		file.write("files/texture/ddiz/btn/end.gif")

ok = open("files/texture/diz/btn/pok.txt", "r").read()
pk = open("files/texture/diz/btn/ppk.txt", "r").read()

ima = open("files/texture/diz/walls/wall.txt", "r").read()
pra = open("files/texture/diz/walls/vpr.txt", "r").read()
ala = open("files/texture/diz/walls/alg.txt", "r").read()
gea = open("files/texture/diz/walls/geo.txt", "r").read()
hia = open("files/texture/diz/walls/him.txt", "r").read()
inia = open("files/texture/diz/walls/inf.txt", "r").read()
nastro = open("files/texture/diz/walls/nas.txt", "r").read()
op = open("files/texture/diz/walls/opro.txt", "r").read()

cvu = open("files/texture/diz/walls/cu.txt", "r").read()

ffff0 = open("files/texture/diz/walls/f_al.txt", "r").read()
ffff1 = open("files/texture/diz/walls/f_fi.txt", "r").read()
ffff2= open("files/texture/diz/walls/f_ge.txt", "r").read()
ffff3 = open("files/texture/diz/walls/f_hi.txt", "r").read()
ffff4 = open("files/texture/diz/walls/f_ma.txt", "r").read()

fal1 = open("files/texture/diz/btn/fal_ap.txt", "r").read()
fal2 = open("files/texture/diz/btn/fal_cu.txt", "r").read()
fal3 = open("files/texture/diz/btn/fal_fsu.txt", "r").read()
fal4 = open("files/texture/diz/btn/fal_gp.txt", "r").read()
fal5 = open("files/texture/diz/btn/fal_op.txt", "r").read()
fal6 = open("files/texture/diz/btn/fal_ps.txt", "r").read()
ffi1 = open("files/texture/diz/btn/ffi_da.txt", "r").read()
ffi2 = open("files/texture/diz/btn/ffi_is.txt", "r").read()
ffi3 = open("files/texture/diz/btn/ffi_it.txt", "r").read()
ffi4 = open("files/texture/diz/btn/ffi_mo.txt", "r").read()
ffi5 = open("files/texture/diz/btn/ffi_ms.txt", "r").read()
ffi6 = open("files/texture/diz/btn/ffi_na.txt", "r").read()
ffi7 = open("files/texture/diz/btn/ffi_pl.txt", "r").read()
ffi8 = open("files/texture/diz/btn/ffi_ra.txt", "r").read()
ffi9 = open("files/texture/diz/btn/ffi_sa.txt", "r").read()
ffi10 = open("files/texture/diz/btn/ffi_se.txt", "r").read()
ffi11 = open("files/texture/diz/btn/ffi_si.txt", "r").read()
ffi12 = open("files/texture/diz/btn/ffi_st.txt", "r").read()
ffi13 = open("files/texture/diz/btn/ffi_us.txt", "r").read()
ffi14 = open("files/texture/diz/btn/ffi_zg.txt", "r").read()
ffi15 = open("files/texture/diz/btn/ffi_zt.txt", "r").read()
ffi16 = open("files/texture/diz/btn/ffi_zn.txt", "r").read()
fge1 = open("files/texture/diz/btn/fge_pt.txt", "r").read()
fge2 = open("files/texture/diz/btn/fge_tc.txt", "r").read()
fge3 = open("files/texture/diz/btn/fge_tp.txt", "r").read()
fge4 = open("files/texture/diz/btn/fge_ts.txt", "r").read()
fhi1 = open("files/texture/diz/btn/fhi_m.txt", "r").read()
fhi2 = open("files/texture/diz/btn/fhi_mmv.txt", "r").read()
fhi3= open("files/texture/diz/btn/fhi_ov.txt", "r").read()
fhi4 = open("files/texture/diz/btn/fhi_pa.txt", "r").read()
fma1 = open("files/texture/diz/btn/fma_fd.txt", "r").read()
fma2 = open("files/texture/diz/btn/fma_fr.txt", "r").read()
fma3 = open("files/texture/diz/btn/fma_fs.txt", "r").read()
fma4 = open("files/texture/diz/btn/fma_pk.txt", "r").read()
fma5 = open("files/texture/diz/btn/fma_pp.txt", "r").read()
fma6 = open("files/texture/diz/btn/fma_pt.txt", "r").read()
fma7 = open("files/texture/diz/btn/fma_ps.txt", "r").read()
fma8 = open("files/texture/diz/btn/fma_ru.txt", "r").read()
fma9 = open("files/texture/diz/btn/fma_ss.txt", "r").read()

tm = open("files/texture/diz/walls/tmh.txt", "r").read()

ppm = open("files/texture/diz/walls/pmsh.txt", "r").read()

plkv = open("files/texture/diz/walls/plk.txt", "r").read()
perkv = open("files/texture/diz/walls/per.txt", "r").read()

ss_vibr = open("files/texture/diz/walls/vibr_ss.txt", "r").read()
ss_sis = open("files/texture/diz/walls/sis_ss.txt", "r").read()

btt = open("files/texture/diz/btn/nach.txt", "r").read()
bttt = open("files/texture/diz/btn/nastr.txt", "r").read()
btttt = open("files/texture/diz/btn/opr.txt", "r").read()

tb = open("files/texture/diz/btn/vtb.txt", "r").read()
tw = open("files/texture/diz/btn/vtw.txt", "r").read()
tnh = open("files/texture/diz/btn/nh.txt", "r").read()
tnp = open("files/texture/diz/btn/np.txt", "r").read()
tnt = open("files/texture/diz/btn/nt.txt", "r").read()
tnw = open("files/texture/diz/btn/nw.txt", "r").read()

pm0 = open("files/texture/diz/btn/pmm.txt", "r").read()
pm1 = open("files/texture/diz/btn/pma.txt", "r").read()
pm2 = open("files/texture/diz/btn/pmg.txt", "r").read()
pm3 = open("files/texture/diz/btn/pmf.txt", "r").read()
pm4 = open("files/texture/diz/btn/pmh.txt", "r").read()

algea = open("files/texture/diz/btn/alg.txt", "r").read()
geoma = open("files/texture/diz/btn/geo.txt", "r").read()
hima = open("files/texture/diz/btn/him.txt", "r").read()
infofa = open("files/texture/diz/btn/inf.txt", "r").read()
prosta = open("files/texture/diz/btn/pro.txt", "r").read()
forma = open("files/texture/diz/btn/for.txt", "r").read()

akva = open("files/texture/diz/btn/kvad.txt", "r").read()

prka = open("files/texture/diz/btn/pk.txt", "r").read()
plka = open("files/texture/diz/btn/plk.txt", "r").read()
prpa = open("files/texture/diz/btn/pp.txt", "r").read()
plpa = open("files/texture/diz/btn/plp.txt", "r").read()
obra = open("files/texture/diz/btn/op.txt", "r").read()

i_ss = open("files/texture/diz/btn/bss.txt", "r").read()

hiha = open("files/texture/diz/btn/hh.txt", "r").read()

pe1 = open("files/texture/diz/btn/p2.txt", "r").read()
pep = open("files/texture/diz/btn/p8.txt", "r").read()
pepe = open("files/texture/diz/btn/p16.txt", "r").read()

cas11 = open("files/texture/diz/citat/an.txt", "r").read()
cas22 = open("files/texture/diz/citat/demo.txt", "r").read()
cas33 = open("files/texture/diz/citat/kon.txt", "r").read()
cas44 = open("files/texture/diz/citat/leo.txt", "r").read()
cas55 = open("files/texture/diz/citat/li.txt", "r").read()
cas66 = open("files/texture/diz/citat/lo.txt", "r").read()
cas77 = open("files/texture/diz/citat/me.txt", "r").read()
cas88 = open("files/texture/diz/citat/pu.txt", "r").read()
cas99 = open("files/texture/diz/citat/sun.txt", "r").read()

undo = open("files/texture/diz/btn/end.txt", "r").read()
reshe = open("files/texture/diz/btn/resh.txt", "r").read()
obaysn = open("files/texture/diz/btn/ob.txt", "r").read()

#Точки
otriz = PhotoImage(file=ok)
sogl = PhotoImage(file=pk)
# ФОН
im = PhotoImage(file=ima)
pr = PhotoImage(file=pra)
al = PhotoImage(file=ala)
ge = PhotoImage(file=gea)
hi = PhotoImage(file=hia)
ini = PhotoImage(file=inia)
nasrt = PhotoImage(file=nastro)
opr = PhotoImage(file=op)
#Геометрия
wplk = PhotoImage(file=plkv)
wprk = PhotoImage(file=perkv)
#Алгебра
ky = PhotoImage(file=cvu)
#Химия
tmh = PhotoImage(file=tm)
#Формулы
pm = PhotoImage(file=ppm)

ff_al = PhotoImage(file=ffff0)
ff_fi = PhotoImage(file=ffff1)
ff_ge = PhotoImage(file=ffff2)
ff_hi = PhotoImage(file=ffff3)
ff_ma = PhotoImage(file=ffff4)

alf1 = PhotoImage(file=fal1)
alf2 = PhotoImage(file=fal2)
alf3 = PhotoImage(file=fal3)
alf4 = PhotoImage(file=fal4)
alf5 = PhotoImage(file=fal5)
alf6 = PhotoImage(file=fal6)

fif1 = PhotoImage(file=ffi1)
fif2 = PhotoImage(file=ffi2)
fif3 = PhotoImage(file=ffi3)
fif4 = PhotoImage(file=ffi4)
fif5 = PhotoImage(file=ffi5)
fif6 = PhotoImage(file=ffi6)
fif7 = PhotoImage(file=ffi7)
fif8 = PhotoImage(file=ffi8)
fif9 = PhotoImage(file=ffi9)
fif10 = PhotoImage(file=ffi10)
fif11 = PhotoImage(file=ffi11)
fif12 = PhotoImage(file=ffi12)
fif13 = PhotoImage(file=ffi13)
fif14 = PhotoImage(file=ffi14)
fif15 = PhotoImage(file=ffi15)
fif16 = PhotoImage(file=ffi16)

gef1 = PhotoImage(file=fge1)
gef2 = PhotoImage(file=fge2)
gef3 = PhotoImage(file=fge3)
gef4 = PhotoImage(file=fge4)


hif1 = PhotoImage(file=fhi1)
hif2 = PhotoImage(file=fhi2)
hif3 = PhotoImage(file=fhi3)
hif4 = PhotoImage(file=fhi4)

maf1 = PhotoImage(file=fma1)
maf2 = PhotoImage(file=fma2)
maf3 = PhotoImage(file=fma3)
maf4 = PhotoImage(file=fma4)
maf5 = PhotoImage(file=fma5)
maf6 = PhotoImage(file=fma6)
maf7 = PhotoImage(file=fma7)
maf8 = PhotoImage(file=fma8)
maf9 = PhotoImage(file=fma9)
#Информатика
vss = PhotoImage(file=ss_vibr)
sss = PhotoImage(file=ss_sis)
# КНОПКИ
#главное меню
bttn = PhotoImage(file=btt)
btttn = PhotoImage(file=bttt)
bttttn = PhotoImage(file=btttt)
#настройки
ntb = PhotoImage(file=tb)
ntw = PhotoImage(file=tw)
nhh = PhotoImage(file=tnh)
np = PhotoImage(file=tnp)
nt = PhotoImage(file=tnt)
nw = PhotoImage(file=tnw)
#выбор предмета
alge = PhotoImage(file=algea)
geom = PhotoImage(file=geoma)
himi = PhotoImage(file=hima)
info = PhotoImage(file=infofa)
prost = PhotoImage(file=prosta)
form = PhotoImage(file=forma)
#алгебра
akv = PhotoImage(file=akva)
#геометрия
prk = PhotoImage(file=prka)
plk = PhotoImage(file=plka)
prp = PhotoImage(file=prpa)
plp = PhotoImage(file=plpa)
obp = PhotoImage(file=obra)
#химия1
hih = PhotoImage(file=hiha)
#информатика 
#pe = PhotoImage(file=pe1)
#per = PhotoImage(file=pep)
#pere = PhotoImage(file=pepe)

iss = PhotoImage(file=i_ss)

#формулы
pmm = PhotoImage(file=pm0)
pma = PhotoImage(file=pm1)
pmg = PhotoImage(file=pm2)
pmf = PhotoImage(file=pm3)
pmh = PhotoImage(file=pm4)

# ЦИТАТЫ
cas1 = PhotoImage(file=cas11)
cas2= PhotoImage(file=cas22)
cas3 = PhotoImage(file=cas33)
cas4 = PhotoImage(file=cas44)
cas5 = PhotoImage(file=cas55)
cas6 = PhotoImage(file=cas66)
cas7 = PhotoImage(file=cas77)
cas8 = PhotoImage(file=cas88)
cas9 = PhotoImage(file=cas99)

#кнопка назад
end = PhotoImage(file=undo)

resh = PhotoImage(file=reshe)
ob = PhotoImage(file=obaysn)

color = open("files/texture/Colors/color.txt", "r").read()
#основной (противоположный фону)
color1 = open("files/texture/Colors/color1.txt", "r").read()
#противоположный
color2 = open("files/texture/Colors/color2.txt", "r").read()
#дополнительный
color3 = open("files/texture/Colors/color3.txt", "r").read()
#дополнительный (соответствующий фону)

def cmb(): #смена на белый цвет
	with open("files/texture/diz/dizain.txt", "w") as file:
		file.write("1")
	yv = messagebox.showinfo("HIS", "Офромление программы измененно \n Перезагрузите программу")

def cmd(): #смена на чёрный цвет
	with open("files/texture/diz/dizain.txt", "w") as file:
		file.write("2")
	yv = messagebox.showinfo("HIS", "Офромление программы измененно \n Перезагрузите программу")

#смена вариантов записи

def snw(): #word
	with open("files/texture/diz/kp.txt", "w") as file:
		file.write("1")
	yv = messagebox.showinfo("HIS", "Ваши изменения сохранены \n Перезагрузите программу")

def snp(): #pdf
	with open("files/texture/diz/kp.txt", "w") as file:
		file.write("2")
	yv = messagebox.showinfo("HIS", "Ваши изменения сохранены \n Перезагрузите программу")

def snt(): #txt
	with open("files/texture/diz/kp.txt", "w") as file:
		file.write("3")
	yv = messagebox.showinfo("HIS", "Ваши изменения сохранены \n Перезагрузите программу")

def snh(): #html
	with open("files/texture/diz/kp.txt", "w") as file:
		file.write("4")
	yv = messagebox.showinfo("HIS", "Ваши изменения сохранены \n Перезагрузите программу")

def himia():
	global lq
	global en
	global nh0
	global nh1
	global nh2
	global nh3
	global nh4
	global nh5
	lq.place_forget()
	en.place_forget()
	nh0.place_forget()
	nh1.place_forget()
	nh2.place_forget()
	nh3.place_forget()
	nh4.place_forget()
	nh5.place_forget()

	global hi
	global end
	global hih

	global lt
	global ent
	global nht
	lt = Label(image=hi)
	lt.place(width=850, height=800, x=0, y=0)
	ent = Button(image=end, bd=0, command=v_himia)
	ent.place(width=64, height=49, x=0, y=0)	
	nht = Button(image=hih, bd=0, command=harakter)
	nht.place(width=427, height=91, x=211, y=155)

def v_himia():
	global lt
	global ent
	global nht
	lt.place_forget()
	ent.place_forget()
	nht.place_forget()
	vibr_pred()

def geometria():
	global lq
	global en
	global nh0
	global nh1
	global nh2
	global nh3
	global nh4
	global nh5
	lq.place_forget()
	en.place_forget()
	nh0.place_forget()
	nh1.place_forget()
	nh2.place_forget()
	nh3.place_forget()
	nh4.place_forget()
	nh5.place_forget()

	global ge
	global end
	global prk
	global plk
	global prp
	global plp
	global obr

	global lr
	global enr
	global nhr
	global nhr1
	global nhr2
	global nhr3
	global nhr4

	lr = Label(image=ge)
	lr.place(width=850, height=800, x=0, y=0)
	enr = Button(image=end, bd=0, command=v_geometria)
	enr.place(width=64, height=49, x=0, y=0)	
	nhr = Button(image=prk, bd=0, command=per_kvad)
	nhr.place(width=427, height=91, x=211, y=145)
	nhr1 = Button(image=plk, bd=0, command=pl_kvad)
	nhr1.place(width=427, height=91, x=211, y=275)
	nhr2 = Button(image=prp, bd=0, command=per_pram)
	nhr2.place(width=427, height=91, x=211, y=407)
	nhr3 = Button(image=plp, bd=0, command=pl_pram)
	nhr3.place(width=427, height=91, x=211, y=535)
	nhr4 = Button(image=obp, bd=0, command=ob_p)
	nhr4.place(width=427, height=91, x=211, y=667)

def v_geometria():
	global lr
	global enr
	global nhr
	global nhr1
	global nhr2
	global nhr3
	global nhr4
	lr.place_forget()
	enr.place_forget()
	nhr.place_forget()
	nhr1.place_forget()
	nhr2.place_forget()
	nhr3.place_forget()
	nhr4.place_forget()
	vibr_pred()

def algebra():
	global lq
	global en
	global nh0
	global nh1
	global nh2
	global nh3
	global nh4
	global nh5
	lq.place_forget()
	en.place_forget()
	nh0.place_forget()
	nh1.place_forget()
	nh2.place_forget()
	nh3.place_forget()
	nh4.place_forget()
	nh5.place_forget()

	global al
	global end
	global asr
	global akv

	global le
	global ene
	global nhe
	global nhe1
	le = Label(image=al)
	le.place(width=850, height=800, x=0, y=0)
	ene = Button(image=end, bd=0, command=v_algebra)
	ene.place(width=64, height=49, x=0, y=0)	
	nhe1 = Button(image=akv, bd=0, command=cv_uy)
	nhe1.place(width=426, height=91, x=212, y=352)

def v_algebra():
	global le
	global ene
	global nhe
	global nhe1
	le.place_forget()
	ene.place_forget()
	nhe1.place_forget()
	vibr_pred()

def vibr_pred():
	global l
	global nach
	global nac
	global nh
	global cl
	l.place_forget()
	nach.place_forget()
	nac.place_forget()
	nh.place_forget()
	cl.place_forget()
	global end
	global im
	global end
	global alge
	global geom
	global himi
	global info
	global prost
	global form

	global lq
	global en
	global nh0
	global nh1
	global nh2
	global nh3
	global nh4
	global nh5

	lq = Label(image=pr)
	lq.place(width=850, height=800, x=0, y=0)
	en = Button(image=end, bd=0, command=v_vibr_pred)
	en.place(width=64, height=49, x=0, y=0)	
	nh0 = Button(bd=0, command=algebra, image=alge)
	nh0.place(width=365, height=89, x=242.5, y=135)
	nh1 = Button(image=geom, bd=0, command=geometria)
	nh1.place(width=365, height=89, x=242.5, y=264)
	nh2 = Button(image=himi, bd=0, command=himia)
	nh2.place(width=365, height=89, x=242.5, y=395)
	nh3 = Button(image=info, bd=0, command=vvod_inf_ss)
	nh3.place(width=365, height=89, x=242.5, y=525)
	nh4 = Button(image=prost, bd=0)
	nh4.place(width=365, height=89, x=28, y=671)
	nh5 = Button(image=form, bd=0, command=visov_formul)
	nh5.place(width=365, height=89, x=460, y=671)

def v_vibr_pred():
	global lq
	global en
	global nh0
	global nh1
	global nh2
	global nh3
	global nh4
	global nh5
	lq.place_forget()
	en.place_forget()
	nh0.place_forget()
	nh1.place_forget()
	nh2.place_forget()
	nh3.place_forget()
	nh4.place_forget()
	nh5.place_forget()
	menu()

def nastroiki():
	global otriz
	global sogl
	global l
	global nach
	global nac
	global nh
	global cl
	global tp

	l.place_forget()
	nach.place_forget()
	nac.place_forget()
	nh.place_forget()
	cl.place_forget()

	global end
	global nastr
	global sost

	global ob1
	global ob2
	global ob3
	global ob4
	global ob5
	global ob6

	global lw
	global enq
	global clq
	global clq0

	global nhh
	global np
	global nt
	global nw
	global ntw
	global ntb

	global n1
	global n2
	global n3
	global n4
	global n5
	global n6

	lw = Label(image=nasrt)
	lw.place(width=850, height=800, x=0, y=0)
	n1 = Button(bd=0, image=nw,  command=snw)
	n1.place(width=190, height=190, x=18, y=213)
	n2 = Button(bd=0, image=np, command=snp)
	n2.place(width=190, height=190, x=226, y=213)
	n3 = Button(bd=0, image=nt, command=snt)
	n3.place(width=190, height=190, x=434, y=213)
	n4 = Button(bd=0, image=nhh, command=snh)
	n4.place(width=190, height=190, x=642, y=213)
	n5 = Button(bd=0, image=ntw, command=cmb)
	n5.place(width=190, height=190, x=18, y=516)
	n6 = Button(bd=0, image=ntb, command=cmd)
	n6.place(width=190, height=190, x=226, y=516)

	if tp == "1":
		ob1 = Label(image=sogl)
		ob1.place(width=19, height=19, x=102, y=377)
	else:
		ob1 = Label(image=otriz)
		ob1.place(width=19, height=19, x=102, y=377)
	
	if tp == "2":
		ob2 = Label(image=sogl)
		ob2.place(width=19, height=19, x=310, y=377)
	else:
		ob2 = Label(image=otriz)
		ob2.place(width=19, height=19, x=310, y=377)
	
	if tp == "3":
		ob3 = Label(image=sogl)
		ob3.place(width=19, height=19, x=519, y=377)
	else:
		ob3 = Label(image=otriz)
		ob3.place(width=19, height=19, x=519, y=377)
	
	if tp == "4":
		ob4 = Label(image=sogl)
		ob4.place(width=19, height=19, x=727, y=377)
	else:
		ob4 = Label(image=otriz)
		ob4.place(width=19, height=19, x=727, y=377)

	if dizain == "1":
		ob5 = Label(image=sogl)
		ob5.place(width=19, height=19, x=102, y=681)
	else:
		ob5 = Label(image=otriz)
		ob5.place(width=19, height=19, x=102, y=681)
	
	if dizain == "2":
		ob6 = Label(image=sogl)
		ob6.place(width=19, height=19, x=310, y=681)
	else:
		ob6 = Label(image=otriz)
		ob6.place(width=19, height=19, x=310, y=681)
	
	enq = Button(image=end, bd=0, command=v_nastroiki)
	enq.place(width=64, height=49, x=0, y=0)

def v_nastroiki():
	global lw
	global enq
	global clq
	global clq0

	global n1
	global n2
	global n3
	global n4
	global n5
	global n6

	global ob1
	global ob2
	global ob3
	global ob4
	global ob5

	lw.place_forget()
	enq.place_forget()
	#
	ob1.place_forget()
	ob2.place_forget()
	ob3.place_forget()
	ob4.place_forget()
	ob5.place_forget()
	ob6.place_forget()

	n1.place_forget()
	n2.place_forget()
	n3.place_forget()
	n4.place_forget()
	n5.place_forget()
	n6.place_forget()

	menu()

def o_programme():
	global l
	global nach
	global nac
	global nh
	global cl
	l.place_forget()
	nach.place_forget()
	nac.place_forget()
	nh.place_forget()
	cl.place_forget()
	global opr
	global IM
	global en1
	IM = Label(image=opr)
	IM.place(width=850, height=800, x=0, y=0)
	en1 = Button(image=end, bd=0, command=v_o_programme)
	en1.place(width=64, height=49, x=0, y=0)

def v_o_programme():
	global IM
	global en1
	IM.place_forget()
	en1.place_forget()
	menu()

def c1():
	global cas1
	global cl
	cl = Label(image=cas1)
	cl.place(width=328, height=172, x=256, y=0)
def c2():
	global cas2
	global cl
	cl = Label(image=cas2)
	cl.place(width=328, height=172, x=256, y=0)
def c3():
	global cas3
	global cl
	cl = Label(image=cas3)
	cl.place(width=328, height=172, x=256, y=0)
def c4():
	global cas4
	global cl
	cl = Label(image=cas4)
	cl.place(width=328, height=172, x=256, y=0)
def c5():
	global cas5
	global cl
	cl = Label(image=cas5)
	cl.place(width=328, height=172, x=256, y=0)
def c6():
	global cl
	global cas6
	cl = Label(image=cas6)
	cl.place(width=328, height=172, x=256, y=0)
def c7():
	global cas7
	global cl
	cl = Label(image=cas7)
	cl.place(width=328, height=172, x=256, y=0)
def c8():
	global cas8
	global cl
	cl = Label(image=cas8)
	cl.place(width=328, height=172, x=256, y=0)
def c9():
	global cas9
	global cl
	cl = Label(image=cas9)
	cl.place(width=328, height=172, x=256, y=0)

def menu():
	global im
	global bttn
	global btttn
	global bttttn

	global l
	global nach
	global nac
	global nh
	global cl
	l = Label(image=im)
	l.place(width=850, height=800, x=0, y=0)
	nach = Button(image=bttn, bd=0, command=vibr_pred)
	nach.place(width=313, height=94, x=270, y=295)	
	nac = Button(image=btttn, bd=0, command=nastroiki)
	nac.place(width=313, height=94, x=270, y=417)
	nh = Button(image=bttttn, bd=0, command=o_programme)
	nh.place(width=313, height=94, x=270, y=540)

	import random
	citata = random.randint(1, 9)

	if citata==1:
		c1()
	if citata==2:
		c2()
	if citata==3:
		c3()
	if citata==4:
		c4()
	if citata==5:
		c5()
	if citata==6:
		c6()
	if citata==7:
		c7()
	if citata==8:
		c8()
	if citata==9:
		c9()

menu()

def pomosh():
	global choice
	if choice==0:
		L = Label(text="В данном режими функция «Объяснение решения» не работает", bg="white", fg="black", font="Arial 10")
		L.place(width=850, height=14, x=0, y=490)
	if choice==1:
		h_h = open("files\pomosh\srav.txt", "r").read()
		Lh = Label(text=h_h, bg="white", font="Arial 14")
		Lh.place(width=850, height=510, x=0, y=0)
	if choice==2:
		h0h = open("files\pomosh\kvad.txt", "r").read()
		Lh1 = Label(text=h0h, bg="white", font="Arial 14")
		Lh1.place(width=850, height=510, x=0, y=0)
	if choice==3:
		h2 = open("files\pomosh\plkvad.txt", "r").read()
		L2 = Label(text=h2, bg=color3, fg=color, font="Arial 14")
		L2.place(width=850, height=100, x=0, y=0)
	if choice==5:
		h3 = open("files\pomosh\perpram.txt", "r").read()
		L3 = Label(text=h3, bg="white", font="Arial 14")
		L3.place(width=850, height=510, x=0, y=0)
	if choice==6:
		h4 = open("files\pomosh\plpram.txt", "r").read()
		L4 = Label(text=h4, bg="white", font="Arial 14")
		L4.place(width=850, height=510, x=0, y=0)	
	if choice==7:
		h5 = open("files\pomosh\paralel.txt", "r").read()
		L5 = Label(text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)	
	if choice==8:
		h5 = open("files\pomosh\dva.txt", "r").read()
		L5 = Label(text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==9:
		h5 = open("files\pomosh/vos.txt", "r").read()
		L5 = Label(text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==10:
		h5 = open("files\pomosh\ses.txt", "r").read()
		L5 = Label(text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==11:
		h5 = open("files\pomosh\slog.txt", "r").read()
		L5 = Label(text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==12:
		h5 = open("files\pomosh/vich.txt", "r").read()
		L5 = Label(text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==13:
		h5 = open("files\pomosh\ymn.txt", "r").read()
		L5 = Label(text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==14:
		h5 = open("files\pomosh\del.txt", "r").read()
		L5 = Label(text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==15:
		h5 = open("files\pomosh\cor.txt", "r").read()
		L5 = Label(text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==16:
		h5 = open("files\pomosh\step.txt", "r").read()
		L5 = Label(text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)

#choice = ""

#•²

# площадь квадрата
def pl_kvad():
	global lr
	global enr
	global nhr
	global nhr1
	global nhr2
	global nhr3
	global nhr4
	lr.place_forget()
	enr.place_forget()
	nhr.place_forget()
	nhr1.place_forget()
	nhr2.place_forget()
	nhr3.place_forget()
	nhr4.place_forget()

	global end
	global resh
	global wprk
	global ob
	global Lor1
	global en1
	global bb1
	global h
	global f
	global l1d1
	global l2d1
	global l3d1
	global l4d1
	global l5d1
	global l6d1
	global l7d1
	global l8d1
	global l9d1
	global l10d1
	global l11d1
	global l12d1
	global l13d1
	global Lh21
	choice = 4
	Lor1 = Label(image=wprk)
	Lor1.place(width=850, height=800, x=0, y=0)
	en1 = Button(image=end, bd=0, command=v_pl_Kvad)
	en1.place(width=64, height=49, x=0, y=0)
	bb1 = Entry(bg=color3, bd=1, fg=color2, font="Arial 18", width=20)
	bb1.place(width=417, height=36, x=11, y=160)
	h = Button(image=resh, bd=0, command=r_pl_kvad)
	h.place(width=348, height=52, x=35, y=258)
	f = Button(image=ob, bd=0, command=p_pl_kvad)
	f.place(width=349, height=52, x=466, y=258)
	l1d1 = Label(bg=color3)
	l1d1.place(width=1, height=1, x=849, y=799)
	l2d1 = Label(bg=color3)
	l2d1.place(width=1, height=1, x=849, y=799)
	l3d1 = Label(bg=color3)
	l3d1.place(width=1, height=1, x=849, y=799)
	l4d1 = Label(bg=color3)
	l4d1.place(width=1, height=1, x=849, y=799)
	l5d1 = Label(bg=color3)
	l5d1.place(width=1, height=1, x=849, y=799)
	l6d1 = Label(bg=color3)
	l6d1.place(width=1, height=1, x=849, y=799)
	l7d1 = Label(bg=color3)
	l7d1.place(width=1, height=1, x=849, y=799)
	l8d1 = Label(bg=color3)
	l8d1.place(width=1, height=1, x=849, y=799)
	l9d1 = Label(bg=color3)
	l9d1.place(width=1, height=1, x=849, y=799)
	l10d1 = Label(bg=color3)
	l10d1.place(width=1, height=1, x=849, y=799)
	l11d1 = Label(bg=color3)
	l11d1.place(width=1, height=1, x=849, y=799)
	l12d1 = Label(bg=color3)
	l12d1.place(width=1, height=1, x=849, y=799)
	l13d1 = Label(bg=color)
	l13d1.place(width=1, height=1, x=849, y=799)
	Lh21 = Label(bg=color)
	Lh21.place(width=1, height=1, x=849, y=799)	

def r_pl_kvad():#event):
	global Lh21
	global l1d1
	global l2d1
	global l3d1
	global l4d1
	global l5d1
	global l6d1
	global l7d1
	global l8d1
	global l9d1
	global l10d1
	global l11d1
	global l12d1
	global l13d1
	Lh21.place_forget()
	l1d1.place_forget()
	l2d1.place_forget()
	l3d1.place_forget()
	l4d1.place_forget()
	l5d1.place_forget()
	l6d1.place_forget()
	l7d1.place_forget()
	l8d1.place_forget()
	l9d1.place_forget()
	l10d1.place_forget()
	l11d1.place_forget()
	l12d1.place_forget()
	l13d1.place_forget()
	try:
		global bb1
		nn = bb1.get()
		resh = int(nn)**2
		y1 = len(nn)
		y2 = len(str(resh))
		otstyp1 = y1*16
		otstyp2 = y2*16
		otstyp3 = otstyp1+35
		#решение
		#root.title("Левая кнопка мыши")
		l1d1 = Label(text="S = ", bg=color3, fg=color2, font="Arial 16")
		l1d1.place(width=35, height=25, x=10, y=510)
		l2d1 = Label(text=nn, bg=color3, fg=color2, font="Arial 16")
		l2d1.place(width=otstyp1, height=25, x=40, y=510)
		l3d1 = Label(text="²", bg=color3, fg=color2, font="Arial 16")
		l3d1.place(width=7, height=25, x=otstyp3, y=510)

		l4d1 = Label(text="S = ", bg=color3, fg=color2, font="Arial 16")
		l4d1.place(width=35, height=25, x=10, y=540)
		l5d1 = Label(text=resh, bg=color3, fg=color2, font="Arial 16")
		l5d1.place(width=otstyp2, height=25, x=45, y=540)

		l6d1 = Label(text="Ответ: S = ", bg=color3, fg=color2, font="Arial 16")
		l6d1.place(width=105, height=25, x=10, y=570)
		l7d1 = Label(text=resh, bg=color3, fg=color2, font="Arial 16")
		l7d1.place(width=otstyp2, height=25, x=115, y=570)
		#метки
		l8d1 = Label(text="a = ", bg=color3, fg=color2, font="Arial 16")
		l8d1.place(width=35, height=25, x=10, y=368)
		l9d1 = Label(text=nn, bg=color3, fg=color2, font="Arial 16")
		l9d1.place(width=otstyp1, height=25, x=45, y=368)
		l10d1 = Label(text="S - ?", bg=color3, fg=color2, font="Arial 16")
		l10d1.place(width=48, height=25, x=298, y=368)
		l11d1 = Label(text="S = a²", bg=color3, fg=color2, font="Arial 16")
		l11d1.place(width=70, height=25, x=578, y=368)
		l12d1 = Label(text=nn, bg=color3, fg=color2, font="Arial 18")
		l12d1.place(width=142, height=25, x=590, y=231)
		l13d1 = Label(text=resh, bg=color3, fg=color2, font="Arial 22")
		l13d1.place(width=140, height=30, x=591, y=150)
		Lh21 = Label(bg=color)
		Lh21.place(width=1, height=1, x=849, y=799)	
	except ValueError:
		error = messagebox.showwarning("HIS", "Вы данном поле возможен только ввод цифр, \n все остальные знаки вводить запрещенно!")

def v_pl_Kvad():
	Lor1.place_forget()
	en1.place_forget()
	bb1.place_forget()
	h.place_forget()
	f.place_forget()
	l1d1.place_forget()
	l2d1.place_forget()
	l3d1.place_forget()
	l4d1.place_forget()
	l5d1.place_forget()
	l6d1.place_forget()
	l7d1.place_forget()
	l8d1.place_forget()
	l9d1.place_forget()
	l10d1.place_forget()
	l11d1.place_forget()
	l12d1.place_forget()
	l13d1.place_forget()
	Lh21.place_forget()
	geometria()

def p_pl_kvad():
	global l1d1
	global l2d1
	global l3d1
	global l4d1
	global l5d1
	global l6d1
	global l7d1
	global l8d1
	global l9d1
	global l10d1
	global l11d1
	global l12d1
	global l13d1
	global Lh21

	l1d1.place_forget()
	l2d1.place_forget()
	l3d1.place_forget()
	l4d1.place_forget()
	l5d1.place_forget()
	l6d1.place_forget()
	l7d1.place_forget()
	l8d1.place_forget()
	l9d1.place_forget()
	l10d1.place_forget()
	l11d1.place_forget()
	l12d1.place_forget()
	l13d1.place_forget()

	Lh21.place_forget()
	h1 = open("files\pomosh\plkvad.txt", "r").read()
	Lh21 = Label(text=h1, bg=color3, fg=color2, font="Arial 15")
	Lh21.place(width=850, height=150, x=0, y=480)

# периметр квадрата

def per_kvad():
	global lr
	global enr
	global nhr
	global nhr1
	global nhr2
	global nhr3
	global nhr4
	lr.place_forget()
	enr.place_forget()
	nhr.place_forget()
	nhr1.place_forget()
	nhr2.place_forget()
	nhr3.place_forget()
	nhr4.place_forget()

	global choice
	global end
	global resh
	global wplk
	global ob
	global Lor
	global en
	global bb
	global h
	global f
	global l1d
	global l2d
	global l3d
	global l4d
	global l5d
	global l6d
	global l7d
	global l8d
	global l9d
	global l10d
	global l11d
	global l12d
	global l13d
	global Lh2
	choice = 4
	Lor = Label(image=wplk)
	Lor.place(width=850, height=800, x=0, y=0)
	en = Button(image=end, bd=0, command=v_per_Kvad)
	en.place(width=64, height=49, x=0, y=0)
	bb = Entry(bg=color3, bd=1, fg=color2, font="Arial 18", width=20)
	bb.place(width=417, height=36, x=11, y=160)
	h = Button(image=resh, bd=0, command=r_pr_kvad)
	h.place(width=348, height=52, x=35, y=258)
	f = Button(image=ob, bd=0, command=p_per_kvad)
	f.place(width=349, height=52, x=466, y=258)
	l1d = Label(bg=color3)
	l1d.place(width=1, height=1, x=849, y=799)
	l2d = Label(bg=color3)
	l2d.place(width=1, height=1, x=849, y=799)
	l3d = Label(bg=color3)
	l3d.place(width=1, height=1, x=849, y=799)
	l4d = Label(bg=color3)
	l4d.place(width=1, height=1, x=849, y=799)
	l5d = Label(bg=color3)
	l5d.place(width=1, height=1, x=849, y=799)
	l6d = Label(bg=color3)
	l6d.place(width=1, height=1, x=849, y=799)
	l7d = Label(bg=color3)
	l7d.place(width=1, height=1, x=849, y=799)
	l8d = Label(bg=color3)
	l8d.place(width=1, height=1, x=849, y=799)
	l9d = Label(bg=color3)
	l9d.place(width=1, height=1, x=849, y=799)
	l10d = Label(bg=color3)
	l10d.place(width=1, height=1, x=849, y=799)
	l11d = Label(bg=color3)
	l11d.place(width=1, height=1, x=849, y=799)
	l12d = Label(bg=color3)
	l12d.place(width=1, height=1, x=849, y=799)
	l13d = Label(bg=color)
	l13d.place(width=1, height=1, x=849, y=799)
	Lh2 = Label(bg=color)
	Lh2.place(width=1, height=1, x=849, y=799)	

def r_pr_kvad():
	global Lh2
	global l1d
	global l2d
	global l3d
	global l4d
	global l5d
	global l6d
	global l7d
	global l8d
	global l9d
	global l10d
	global l11d
	global l12d
	global l13d
	Lh2.place_forget()
	l1d.place_forget()
	l2d.place_forget()
	l3d.place_forget()
	l4d.place_forget()
	l5d.place_forget()
	l6d.place_forget()
	l7d.place_forget()
	l8d.place_forget()
	l9d.place_forget()
	l10d.place_forget()
	l11d.place_forget()
	l12d.place_forget()
	l13d.place_forget()
	try:
		global bb
		nn = bb.get()
		resh = int(nn)*4
		y1 = len(nn)
		y2 = len(str(resh))
		otstyp1 = y1*16
		otstyp2 = y2*16
		otstyp3 = otstyp1+35
		#решение
		l1d = Label(text="P = ", bg=color3, fg=color2, font="Arial 16")
		l1d.place(width=35, height=25, x=10, y=510)
		l2d = Label(text=nn, bg=color3, fg=color2, font="Arial 16")
		l2d.place(width=otstyp1, height=25, x=40, y=510)
		l3d = Label(text="• 4", bg=color3, fg=color2, font="Arial 16")
		l3d.place(width=40, height=25, x=otstyp3, y=510)

		l4d = Label(text="P = ", bg=color3, fg=color2, font="Arial 16")
		l4d.place(width=35, height=25, x=10, y=540)
		l5d = Label(text=resh, bg=color3, fg=color2, font="Arial 16")
		l5d.place(width=otstyp2, height=25, x=45, y=540)

		l6d = Label(text="Ответ: P = ", bg=color3, fg=color2, font="Arial 16")
		l6d.place(width=105, height=25, x=10, y=570)
		l7d = Label(text=resh, bg=color3, fg=color2, font="Arial 16")
		l7d.place(width=otstyp2, height=25, x=115, y=570)
		#метки
		l8d = Label(text="a = ", bg=color3, fg=color2, font="Arial 16")
		l8d.place(width=35, height=25, x=10, y=368)
		l9d = Label(text=nn, bg=color3, fg=color2, font="Arial 16")
		l9d.place(width=otstyp1, height=25, x=45, y=368)
		l10d = Label(text="P - ?", bg=color3, fg=color2, font="Arial 16")
		l10d.place(width=48, height=25, x=298, y=368)
		l11d = Label(text="P = 4a", bg=color3, fg=color2, font="Arial 16")
		l11d.place(width=70, height=25, x=578, y=368)
		l12d = Label(text=nn, bg=color3, fg=color2, font="Arial 18")
		l12d.place(width=142, height=25, x=590, y=231)
		l13d = Label(text=resh, bg=color3, fg=color2, font="Arial 22")
		l13d.place(width=140, height=30, x=591, y=150)
		Lh2 = Label(bg=color)
		Lh2.place(width=1, height=1, x=849, y=799)	
	except ValueError:
		error = messagebox.showwarning("HIS", "Вы данном поле возможен только ввод цифр, \n все остальные знаки вводить запрещено!")

def v_per_Kvad():
	Lor.place_forget()
	en.place_forget()
	bb.place_forget()
	h.place_forget()
	f.place_forget()
	l1d.place_forget()
	l2d.place_forget()
	l3d.place_forget()
	l4d.place_forget()
	l5d.place_forget()
	l6d.place_forget()
	l7d.place_forget()
	l8d.place_forget()
	l9d.place_forget()
	l10d.place_forget()
	l11d.place_forget()
	l12d.place_forget()
	l13d.place_forget()
	Lh2.place_forget()
	geometria()

def p_per_kvad():
	global l1d
	global l2d
	global l3d
	global l4d
	global l5d
	global l6d
	global l7d
	global l8d
	global l9d
	global l10d
	global l11d
	global l12d
	global l13d
	global Lh2

	l1d.place_forget()
	l2d.place_forget()
	l3d.place_forget()
	l4d.place_forget()
	l5d.place_forget()
	l6d.place_forget()
	l7d.place_forget()
	l8d.place_forget()
	l9d.place_forget()
	l10d.place_forget()
	l11d.place_forget()
	l12d.place_forget()
	l13d.place_forget()

	Lh2.place_forget()
	h1 = open("files\pomosh\perkvad.txt", "r").read()
	Lh2 = Label(text=h1, bg=color3, fg=color2, font="Arial 15")
	Lh2.place(width=850, height=150, x=0, y=480)

# периметр прямоугольника
def per_pram():
	#убрать заполнение автоформ
	#переписать разделы геометрии

	#global end
	en = Button(image=end, bd=0, command=geometria)
	en.place(width=64, height=49, x=0, y=0)	
	global choice
	choice = 5

	#	lab = Label(text="Введите длину сторон:", bg="white", fg="MediumBluE", font="Arial 22")
	#	lab.place(width=850, height=40, x=0, y=5)
	# без указания глобальных переменных кодж выдаёт ошибку в коде есть ссылка на глобальную переменную между функциями
	global bb
	#	ov = Label(text="Введите сторону a:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	#	ov.place(width=120, height=20, x=0, y=40)
	bb = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	bb.place(width=100, height=16, x=120, y=44)
	global bbb
	#	vo = Label(text="Введите сторону b:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	#	vo.place(width=120, height=20, x=0, y=60)
	bbb = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	bbb.place(width=100, height=16, x=120, y=64)

	kresh = Button(text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=r_per_pram)
	kresh.place(width=120, height=30, x=362, y=170)
	
	#	lb = Label(text="Решение:", bg="white", fg="MediumBluE", font="Arial 22")
	#	lb.place(width=850, height=40, x=0, y=5)

def r_per_pram():
	global bb
	nn = bb.get()
	global bbb
	nnn = bbb.get()
	resh = (int(nn)+int(nnn))*2
	rash = int(nn)+int(nnn)
	y1 = len(nn)
	y2 = len(nnn)
	y3 = len(str(resh))
	otstyp1 = y1*9
	otstyp2 = y2*9
	otstyp3 = y3*9
	otstyp5 = otstyp1+15
	otstyp6 = otstyp5+10
	otstyp7 = otstyp6+otstyp2
	otstyp8 = otstyp7+10
	otstyp9 = otstyp1+35
	otstyp0 = otstyp1+25
	l1d = Label(text="По формуле:S=2(a•b)", bg="white", fg="black", font="Arial 12")
	l1d.place(width=155, height=25, x=0, y=50)

	l2d = Label(text="S=", bg="white", fg="black", font="Arial 12")
	l2d.place(width=15, height=25, x=1, y=75)
	l3d = Label(text=nn, bg="white", fg="black", font="Arial 12")
	l3d.place(width=otstyp1, height=25, x=15, y=75)
	l4d = Label(text="+", bg="white", fg="black", font="Arial 12")
	l4d.place(width=10, height=25, x=otstyp5, y=75)
	l4d = Label(text=nnn, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp2, height=25, x=otstyp6, y=75)
	l5d = Label(text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=10, height=25, x=otstyp7, y=75)
	l6d = Label(text=rash, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp3, height=25, x=otstyp8, y=75)

	l2d = Label(text="S=", bg="white", fg="black", font="Arial 12")
	l2d.place(width=15, height=25, x=1, y=100)
	l3d = Label(text=rash, bg="white", fg="black", font="Arial 12")
	l3d.place(width=otstyp1, height=25, x=15, y=100)
	l4d = Label(text="•", bg="white", fg="black", font="Arial 12")
	l4d.place(width=10, height=25, x=otstyp5, y=100)
	l4d = Label(text="2", bg="white", fg="black", font="Arial 12")
	l4d.place(width=10, height=25, x=otstyp6, y=100)
	l5d = Label(text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=20, height=25, x=otstyp9, y=100)
	l6d = Label(text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp9, height=25, x=otstyp9, y=100)

	l7d = Label(text="Ответ: S=", bg="white", fg="black", font="Arial 12")
	l7d.place(width=70, height=25, x=2, y=125)
	l8d = Label(text=resh, bg="white", fg="black", font="Arial 12")
	l8d.place(width=otstyp3, height=25, x=75, y=125)

# площадь прямоугольника
def pl_pram():
	global end
	en = Button(image=end, bd=0, command=geometria)
	en.place(width=64, height=49, x=0, y=0)	
	global choice
	choice = 6
	lab = Label(text="Введите длину сторон:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global mm
	ov = Label(text="Введите сторону a:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	ov.place(width=120, height=20, x=0, y=40)
	mm = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	mm.place(width=100, height=16, x=120, y=44)
	global mmm
	vo = Label(text="Введите сторону b:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	vo.place(width=120, height=20, x=0, y=60)
	mmm = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	mmm.place(width=100, height=16, x=120, y=64)

	kresh = Button(text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=r_pl_pram)
	kresh.place(width=120, height=30, x=362, y=170)
	
	lb = Label(text="Решение:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)

def r_pl_pram():
	global mm
	nn = mm.get()
	global mmm
	nnn = mmm.get()
	resh = int(nn)*int(nnn)
	y1 = len(nn)
	y2 = len(nnn)
	y3 = len(str(resh))
	otstyp1 = y1*9
	otstyp2 = y2*9
	otstyp3 = y3*9
	otstyp5 = otstyp1+15
	otstyp6 = otstyp5+10
	otstyp7 = otstyp6+otstyp2
	otstyp8 = otstyp7+10
	l1d = Label(text="По формуле:S=a•b", bg="white", fg="black", font="Arial 12")
	l1d.place(width=150, height=25, x=0, y=50)
	l2d = Label(text="S=", bg="white", fg="black", font="Arial 12")
	l2d.place(width=15, height=25, x=0, y=75)
	l3d = Label(text=nn, bg="white", fg="black", font="Arial 12")
	l3d.place(width=otstyp1, height=25, x=15, y=75)
	l4d = Label(text="•", bg="white", fg="black", font="Arial 12")
	l4d.place(width=10, height=25, x=otstyp5, y=75)
	l4d = Label(text=nnn, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp2, height=25, x=otstyp6, y=75)
	l5d = Label(text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=10, height=25, x=otstyp7, y=75)
	l6d = Label(text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp3, height=25, x=otstyp8, y=75)
	l7d = Label(text="Ответ: S=", bg="white", fg="black", font="Arial 12")
	l7d.place(width=70, height=25, x=2, y=100)
	l8d = Label(text=resh, bg="white", fg="black", font="Arial 12")
	l8d.place(width=otstyp3, height=25, x=75, y=100)

# объём параллелепипеда
def ob_p():
	global end
	en = Button(image=end, bd=0, command=geometria)
	en.place(width=64, height=49, x=0, y=0)	
	global choice
	choice = 7

	lab = Label(text="Введите длину сторон:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global cc
	ov = Label(text="Введите сторону a:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	ov.place(width=120, height=20, x=0, y=40)
	cc = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	cc.place(width=100, height=16, x=120, y=44)
	global ccc
	vo = Label(text="Введите сторону b:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	vo.place(width=120, height=20, x=0, y=60)
	ccc = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	ccc.place(width=100, height=16, x=120, y=64)

	global c
	ov = Label(text="Введите сторону c:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	ov.place(width=120, height=20, x=0, y=80)
	c = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	c.place(width=100, height=16, x=120, y=84)

	kresh = Button(text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=r_ob_p)
	kresh.place(width=120, height=30, x=362, y=170)
	
	lb = Label(text="Решение:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)

def r_ob_p():
	global cc
	nn = cc.get()
	global ccc
	nnn = ccc.get()
	global c
	n = c.get()
	resh = int(nn)*int(nnn)*int(n)
	y1 = len(nn)
	y2 = len(nnn)
	y0 = len(n)
	y3 = len(str(resh))
	otstyp1 = y1*9
	otstyp2 = y2*9
	otstyp3 = y3*9
	otstyp4 = y0*9
	otstyp5 = otstyp1+15
	otstyp6 = otstyp5+10
	otstyp9 = otstyp6+otstyp2
	otstyp7 = otstyp9+otstyp4
	otstyp8 = otstyp7+otstyp4
	otstyp0 = otstyp8+otstyp3
	l1d = Label(text="По формуле:V=a•b•c", bg="white", fg="black", font="Arial 12")
	l1d.place(width=155, height=25, x=0, y=50)
	l2d = Label(text="V=", bg="white", fg="black", font="Arial 12")
	l2d.place(width=15, height=25, x=0, y=75)
	l3d = Label(text=nn, bg="white", fg="black", font="Arial 12")
	l3d.place(width=otstyp1, height=25, x=15, y=75)
	l4d = Label(text="•", bg="white", fg="black", font="Arial 12")
	l4d.place(width=10, height=25, x=otstyp5, y=75)
	l4d = Label(text=nnn, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp2, height=25, x=otstyp6, y=75)
	l4d = Label(text="•", bg="white", fg="black", font="Arial 12")
	l4d.place(width=10, height=25, x=otstyp9, y=75)
	l4d = Label(text=n, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp4, height=25, x=otstyp7, y=75)

	l5d = Label(text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=10, height=25, x=otstyp8, y=75)
	l6d = Label(text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp3, height=25, x=otstyp0, y=75)

	l7d = Label(text="Ответ: V=", bg="white", fg="black", font="Arial 12")
	l7d.place(width=70, height=25, x=2, y=100)
	l8d = Label(text=resh, bg="white", fg="black", font="Arial 12")
	l8d.place(width=otstyp3, height=25, x=75, y=100)

# А Л Г Е Б Р А
# А Л Г Е Б Р А
# А Л Г Е Б Р А
# А Л Г Е Б Р А
# А Л Г Е Б Р А

#квадратное уравнение
def cv_uy():
	global le
	global ene
	global nhe
	global nhe1

	le.place_forget()
	ene.place_forget()
	nhe1.place_forget()

	global choice
	global end
	global resh
	global wplk
	global ob
	global Lor
	global en
	global bb
	global bb1
	global bb2
	global h
	global f
	global l1d
	global l2d
	global l3d
	global l4d
	global l5d
	global l6d
	global l7d
	global l8d
	global l9d
	global l10d
	global l11d
	global l12d
	global l13d
	global l14d
	global l15d
	global l16d
	global l17d
	global l18d

	global Lh2
	global ckv1
	global ckv2
	global ckv3

	global hh11
	global hh12

	#choice = 

	Lor = Label(image=ky)
	Lor.place(width=850, height=800, x=0, y=0)

	en = Button(image=end, bd=0, command=v_cv_uy)
	en.place(width=64, height=49, x=0, y=0)

	bb = Entry(bg=color3, bd=1, fg=color2, font="Arial 18", width=20)
	bb.place(width=326, height=30, x=15, y=113)
	bb1 = Entry(bg=color3, bd=1, fg=color2, font="Arial 18", width=20)
	bb1.place(width=326, height=30, x=15, y=191)
	bb2 = Entry(bg=color3, bd=1, fg=color2, font="Arial 18", width=20)
	bb2.place(width=326, height=30, x=15, y=271)

	hh11 = Checkbutton(text="Дискриминант", bd=0, bg=color3, justify="left", fg=color2, activebackground=color, 
		font="Cambria 20", activeforeground=color3, command=kvad_yr1)
	hh11.place(width=350, height=30, x=450, y=113)
	hh12 = Checkbutton(text="Свойства коэффициентов", bd=0,  bg=color3, justify="left", fg=color2, activebackground=color, 
		font="Cambria 20", activeforeground=color3, command=kvad_yr2)
	hh12.place(width=350, height=30, x=450, y=191)
	#hh13 = Checkbutton(text="Теорема Виета", bd=0,  bg=color3, justify="left", fg=color2, activebackground=color, 
	#	font="Cambria 20", activeforeground=color3, command=kvad_yr3)
	#hh13.place(width=350, height=30, x=450, y=271)

	h = Button(image=resh, bd=0, command=r_cv_uy)
	h.place(width=348, height=52, x=35, y=328)
	f = Button(image=ob, bd=0, command=p_cv_uy)
	f.place(width=349, height=52, x=466, y=328)

	ckv1 = 0
	ckv2 = 0
	#ckv3 = 0

	l1d = Label(bg=color3)
	l1d.place(width=1, height=1, x=849, y=799)
	l2d = Label(bg=color3)
	l2d.place(width=1, height=1, x=849, y=799)
	l3d = Label(bg=color3)
	l3d.place(width=1, height=1, x=849, y=799)
	l4d = Label(bg=color3)
	l4d.place(width=1, height=1, x=849, y=799)
	l5d = Label(bg=color3)
	l5d.place(width=1, height=1, x=849, y=799)
	l6d = Label(bg=color3)
	l6d.place(width=1, height=1, x=849, y=799)
	l7d = Label(bg=color3)
	l7d.place(width=1, height=1, x=849, y=799)
	l8d = Label(bg=color3)
	l8d.place(width=1, height=1, x=849, y=799)
	l9d = Label(bg=color3)
	l9d.place(width=1, height=1, x=849, y=799)
	l10d = Label(bg=color3)
	l10d.place(width=1, height=1, x=849, y=799)
	l11d = Label(bg=color3)
	l11d.place(width=1, height=1, x=849, y=799)
	l12d = Label(bg=color3)
	l12d.place(width=1, height=1, x=849, y=799)
	l13d = Label(bg=color)
	l13d.place(width=1, height=1, x=849, y=799)
	l14d = Label(bg=color3)
	l14d.place(width=1, height=1, x=849, y=799)
	l15d = Label(bg=color3)
	l15d.place(width=1, height=1, x=849, y=799)
	l16d = Label(bg=color3)
	l16d.place(width=1, height=1, x=849, y=799)
	l17d = Label(bg=color3)
	l17d.place(width=1, height=1, x=849, y=799)
	l18d = Label(bg=color)
	l18d.place(width=1, height=1, x=849, y=799)
	Lh2 = Label(bg=color)
	Lh2.place(width=1, height=1, x=849, y=799)	

def kvad_yr1():
	global ckv1
	ckv1 = 1
def kvad_yr2():
	global ckv2
	ckv2 = 1 
#def kvad_yr3():
	global ckv3
	ckv3 = 1 

def r_cv_uy():
	global bb
	global bb1
	global bb2

	global hh11
	global hh12

	if bb == "0":
		messagebox.showwarning("HIS", "Вы ввели не квадратное уравнение!")
	if bb1 == "0":
		messagebox.showwarning("HIS", "Вы ввели не квадратное уравнение!")
	if bb2 == "0":
		messagebox.showwarning("HIS", "Вы ввели не квадратное уравнение!")
	
	global ckv1
	global ckv2
	global ckv3
	global Lh2
	global l1d
	global l2d
	global l3d
	global l4d
	global l5d
	global l6d
	global l7d
	global l8d
	global l9d
	global l10d
	global l11d
	global l12d
	global l13d
	global l14d
	global l15d
	global l16d
	global l17d
	global l18d
	global l19d
	global l20d
	global l21d
	global l22d
	global l23d
	global l24d
	global l25d
	global l26d
	global l27d
	global l28d
	global l29d
	global l30d
	global l31d
	global l32d
	global l33d
	global l34d
	global l35d
	global l36d
	global l37d
	global l38d
	global l39d
	global color1

	#hh11.place_forget()
	#hh12.place_forget()

	Lh2.place_forget()
	l1d.place_forget()
	l2d.place_forget()
	l3d.place_forget()
	l4d.place_forget()
	l5d.place_forget()
	l6d.place_forget()
	l7d.place_forget()
	l8d.place_forget()
	l9d.place_forget()
	l10d.place_forget()
	l11d.place_forget()
	l12d.place_forget()
	l13d.place_forget()
	l14d.place_forget()
	l15d.place_forget()
	l16d.place_forget()
	l17d.place_forget()
	l18d.place_forget()

	try:
		pr10 = 0
		pr11 = 0
		pr01 = 0

		#вычисление введённых способов решения
	#	if ckv1 == 0 and ckv2 == 0 and ckv3 == 0:
	#		messagebox.showwarning("HIS", "Вы не выбрали способ решения, \n квадратного уравнения!")
	#	elif ckv1 == 1 and ckv2 == 0 and ckv3 == 0:
	#			pr10 = 1
	#	elif ckv1 == 0 and ckv2 == 1 and ckv3 == 0:
	#		pr10 = 2
	#	elif ckv1 == 0 and ckv2 == 0 and ckv3 == 1:
	#		pr10 = 3
	#	elif ckv1 == 1 and ckv2 == 1 and ckv3 == 1:
	#		pr10 = 0
	#	elif ckv1 == 0 and ckv2 == 1 and ckv3 == 1:
	#		pr10 = 4
	#	elif ckv1 == 1 and ckv2 == 1 and ckv3 == 0:
	#		pr10 = 5

		if ckv1 == 0 and ckv2 == 0:
			messagebox.showwarning("HIS", "Вы не выбрали способ решения, \n квадратного уравнения!")
		elif ckv1 == 1 and ckv2 == 0:
			pr10 = 1
		elif ckv1 == 0 and ckv2 == 1:
			pr10 = 2
		elif ckv1 == 1 and ckv2 == 1:
			pr10 = 3

			
		ba = bb.get()
		bbb = bb1.get()
		bc = bb2.get()

		#1 и 2 способ
		if pr10 == 2:
			ba = bb.get()
			bbb = bb1.get()
			bc = bb2.get()
			summ1 = int(ba)+int(bbb)+int(bc)
			summ2 = int(ba)+int(bc)
			if summ1 == 0:
				rz1=1
			else:
				rz1=0
		
			if summ2 == int(bbb):
				rz2=1
			else:
				rz2=2

			#окончательный вердикт проверки
			if rz1 == 1 or rz2 == 1:
				verd=1
			else:
				verd=0
				messagebox.showwarning("HIS", "Данное уравнение невозможно решить, \n методом коэффециентов!")


		#решение методом коэффециентов
		if pr10 == 2:
			if rz1 == 1:
				ya = len(ba)*10
				yb = len(bbb)*10
				yc = len(bc)*10

				otstyp1 = ya + 17
				otstyp2 = otstyp1 + 10
				otstyp22 = otstyp2 + 10
				otstyp3 = otstyp2 + yb + 10
				otstyp4 = otstyp3 + 10 + 10
				otstyp5 = otstyp2 + yc + 10
				otstyp6 = otstyp5 + 10 + 10
				otstyp7 = otstyp6 + yc + 10
				l1d = Label(text=ba, bg=color3, fg=color1, font="Arial 12")
				l1d.place(width=ya, height=16, x=0, y=400)
				l2d = Label(text="X²", bg=color3, fg=color1, font="Arial 12")
				l2d.place(width=17, height=16, x=ya, y=400)

				if int(bbb) > 0:
					l3d = Label(text="+", bg=color3, fg=color1, font="Arial 12")
					l3d.place(width=10, height=16, x=otstyp1, y=400)
					l4d = Label(text=bbb, bg=color3, fg=color1, font="Arial 12")
					l4d.place(width=yb, height=16, x=otstyp2, y=400)

				if int(bbb) < 0:
					tyu = int(bbb) *(-1)
					tyt = yb - 10
					l3d = Label(text="-", bg=color3, fg=color1, font="Arial 12")
					l3d.place(width=10, height=16, x=otstyp1, y=400)
					l4d = Label(text=tyu, bg=color3, fg=color1, font="Arial 12")
					l4d.place(width=tyt, height=16, x=otstyp2, y=400)
				
				l5d = Label(text="X", bg=color3, fg=color1, font="Arial 12")
				l5d.place(width=10, height=16, x=otstyp22, y=400)

				if int(bc) > 0:
					l6d = Label(text="+", bg=color3, fg=color1, font="Arial 12")
					l6d.place(width=10, height=16, x=otstyp3, y=400)
					l7d = Label(text=bc, bg=color3, fg=color1, font="Arial 12")
					l7d.place(width=yc, height=16, x=otstyp4, y=400)
				
				if int(bc) < 0:
					tyo = int(bc) *(-1)
					typ = yc - 10
					l6d = Label(text="-", bg=color3, fg=color1, font="Arial 12")
					l6d.place(width=10, height=16, x=otstyp5, y=400)
					l7d = Label(text=tyo, bg=color3, fg=color1, font="Arial 12")
					l7d.place(width=typ, height=16, x=otstyp6, y=400)

				l8d = Label(text="=0", bg=color3, fg=color1, font="Arial 12")
				l8d.place(width=20, height=16, x=otstyp7, y=400)
				l9d = Label(text="Метод коэффициентов:", bg=color3, fg=color1, font="Arial 12")
				l9d.place(width=172, height=16, x=0, y=420)
				l10d = Label(text="A+B+C=0", bg=color3, fg=color1, font="Arial 12")
				l10d.place(width=70, height=16, x=0, y=440)
				l11d = Label(text="По 1 свойству коэффициентов:", bg=color3, fg=color1, font="Arial 12")
				l11d.place(width=226, height=16, x=0, y=460)
				l12d = Label(text="X₁=1", bg=color3, fg=color1, font="Arial 12")
				l12d.place(width=40, height=16, x=0, y=480)
				l13d = Label(text="X₂=C/A", bg=color3, fg=color1, font="Arial 12")
				l13d.place(width=60, height=16, x=0, y=500)
				l14d = Label(text="X₁=1", bg=color3, fg=color1, font="Arial 12")
				l14d.place(width=40, height=16, x=0, y=540)
				l15d = Label(text="X₂=", bg=color3, fg=color1, font="Arial 12")
				l15d.place(width=30, height=16, x=0, y=560)

				#вычисление второго X
				ch1 = int(ba)
				ch2 = int(bc)
				otv1 = ch2/ch1
				hz = str(otv1)
				otstyp110 = len(hz)*9
				l16d = Label(text=otv1, bg=color3, fg=color1, font="Arial 12")
				l16d.place(width=otstyp110, height=16, x=30, y=560)

				#Ответ
				l17d = Label(text="Ответ: 1;", bg=color3, fg=color1, font="Arial 12")
				l17d.place(width=65, height=16, x=0, y=600)
				l18d = Label(text=otv1, bg=color3, fg=color1, font="Arial 12")
				l18d.place(width=otstyp110, height=16, x=65, y=600)

			if rz2 == 1:
				ya = len(ba)*10
				yb = len(bbb)*10
				yc = len(bc)*10

				otstyp1 = ya + 17
				otstyp2 = otstyp1 + 10
				otstyp22 = otstyp2 + 10
				otstyp3 = otstyp2 + yb + 10
				otstyp4 = otstyp3 + 10 + 10
				otstyp5 = otstyp2 + yc + 10
				otstyp6 = otstyp5 + 10 + 10
				otstyp7 = otstyp6 + yc + 10
				l1d = Label(text=ba, bg=color3, fg=color1, font="Arial 12")
				l1d.place(width=ya, height=16, x=0, y=400)
				l2d = Label(text="X²", bg=color3, fg=color1, font="Arial 12")
				l2d.place(width=17, height=16, x=ya, y=400)

				if int(bbb) > 0:
					l3d = Label(text="+", bg=color3, fg=color1, font="Arial 12")
					l3d.place(width=10, height=16, x=otstyp1, y=400)
					l4d = Label(text=bbb, bg=color3, fg=color1, font="Arial 12")
					l4d.place(width=yb, height=16, x=otstyp2, y=400)

				if int(bbb) < 0:
					tyu = int(bbb) *(-1)
					tyt = yb - 10
					l3d = Label(text="-", bg=color3, fg=color1, font="Arial 12")
					l3d.place(width=10, height=16, x=otstyp1, y=400)
					l4d = Label(text=tyu, bg=color3, fg=color1, font="Arial 12")
					l4d.place(width=tyt, height=16, x=otstyp2, y=400)
				
				l5d = Label(text="X", bg=color3, fg=color1, font="Arial 12")
				l5d.place(width=10, height=16, x=otstyp22, y=400)

				if int(bc) > 0:
					l6d = Label(text="+", bg=color3, fg=color1, font="Arial 12")
					l6d.place(width=10, height=16, x=otstyp3, y=400)
					l7d = Label(text=bc, bg=color3, fg=color1, font="Arial 12")
					l7d.place(width=yc, height=16, x=otstyp4, y=400)
				
				if int(bc) < 0:
					tyo = int(bc) *(-1)
					typ = yc - 10
					l6d = Label(text="-", bg=color3, fg=color1, font="Arial 12")
					l6d.place(width=10, height=16, x=otstyp5, y=400)
					l7d = Label(text=tyo, bg=color3, fg=color1, font="Arial 12")
					l7d.place(width=typ, height=16, x=otstyp6, y=400)

				l8d = Label(text="=0", bg=color3, fg=color1, font="Arial 12")
				l8d.place(width=20, height=16, x=otstyp7, y=400)
				l9d = Label(text="Метод коэффициентов:", bg=color3, fg=color1, font="Arial 12")
				l9d.place(width=172, height=16, x=0, y=420)
				l10d = Label(text="A+C=B", bg=color3, fg=color1, font="Arial 12")
				l10d.place(width=54, height=16, x=0, y=440)
				l11d = Label(text="По 2 свойству коэффициентов:", bg=color3, fg=color1, font="Arial 12")
				l11d.place(width=226, height=16, x=0, y=460)
				l12d = Label(text="X₁=-1", bg=color3, fg=color1, font="Arial 12")
				l12d.place(width=45, height=16, x=0, y=480)
				l13d = Label(text="X₂=-C/A", bg=color3, fg=color1, font="Arial 12")
				l13d.place(width=65, height=16, x=0, y=500)
				l14d = Label(text="X₁=-1", bg=color3, fg=color1, font="Arial 12")
				l14d.place(width=45, height=16, x=0, y=540)
				l15d = Label(text="X₂=", bg=color3, fg=color1, font="Arial 12")
				l15d.place(width=30, height=16, x=0, y=560)

				#вычисление второго X
				ch1 = int(ba)
				ch1_1= int(bc)
				ch2 = ch1_1 * (-1)
				otv1 = ch2/ch1
				hz = str(otv1)
				otstyp110 = len(hz)*9
				l16d = Label(text=otv1, bg=color3, fg=color1, font="Arial 12")
				l16d.place(width=otstyp110, height=16, x=30, y=560)

				#Ответ
				l17d = Label(text="Ответ: -1;", bg=color3, fg=color1, font="Arial 12")
				l17d.place(width=70, height=16, x=0, y=600)
				l18d = Label(text=otv1, bg=color3, fg=color1, font="Arial 12")
				l18d.place(width=otstyp110, height=16, x=70, y=600)

				l19d = Label(bg=color3)
				l19d.place(width=1, height=1, x=849, y=799)
				l20d = Label(bg=color3)
				l20d.place(width=1, height=1, x=849, y=799)
				l21d = Label(bg=color3)
				l21d.place(width=1, height=1, x=849, y=799)
				l22d = Label(bg=color3)
				l22d.place(width=1, height=1, x=849, y=799)
				l23d = Label(bg=color3)
				l23d.place(width=1, height=1, x=849, y=799)
				l24d = Label(bg=color3)
				l24d.place(width=1, height=1, x=849, y=799)	
				l25d = Label(bg=color3)
				l25d.place(width=1, height=1, x=849, y=799)
				l26d = Label(bg=color3)
				l26d.place(width=1, height=1, x=849, y=799)
				l27d = Label(bg=color3)
				l27d.place(width=1, height=1, x=849, y=799)
				l28d = Label(bg=color3)
				l28d.place(width=1, height=1, x=849, y=799)
				l29d = Label(bg=color3)
				l29d.place(width=1, height=1, x=849, y=799)
				l30d = Label(bg=color3)
				l30d.place(width=1, height=1, x=849, y=799)
				l31d = Label(bg=color3)
				l31d.place(width=1, height=1, x=849, y=799)
				l32d = Label(bg=color3)
				l32d.place(width=1, height=1, x=849, y=799)
				l33d = Label(bg=color3)
				l33d.place(width=1, height=1, x=849, y=799)
				l34d = Label(bg=color3)
				l34d.place(width=1, height=1, x=849, y=799)
				l35d = Label(bg=color3)
				l35d.place(width=1, height=1, x=849, y=799)
				l36d = Label(bg=color3)
				l36d.place(width=1, height=1, x=849, y=799)
				l37d = Label(bg=color3)
				l37d.place(width=1, height=1, x=849, y=799)
				l38d = Label(bg=color3)
				l38d.place(width=1, height=1, x=849, y=799)
				l39d = Label(bg=color3)
				l39d.place(width=1, height=1, x=849, y=799)

		#дискриминант
		if pr10 == 1 or pr10 == 3:# or pr10 == 5:
			ba = bb.get()
			bbb = bb1.get()
			bc = bb2.get()
			ya = len(ba)*10
			yb = len(bbb)*10
			yc = len(bc)*10

			otstyp1 = ya + 17
			otstyp2 = otstyp1 + 10
			otstyp22 = otstyp2 + 10
			otstyp3 = otstyp2 + yb + 10
			otstyp4 = otstyp3 + 10 + 10
			otstyp5 = otstyp2 + yc + 10			
			otstyp6 = otstyp5 + 10 + 10
			otstyp7 = otstyp6 + yc + 10
			l1d = Label(text=ba, bg=color3, fg=color1, font="Arial 12")
			l1d.place(width=ya, height=16, x=0, y=400)
			l2d = Label(text="X²", bg=color3, fg=color1, font="Arial 12")
			l2d.place(width=17, height=16, x=ya, y=400)

			if int(bbb) > 0:
				l3d = Label(text="+", bg=color3, fg=color1, font="Arial 12")
				l3d.place(width=10, height=16, x=otstyp1, y=400)
				l4d = Label(text=bbb, bg=color3, fg=color1, font="Arial 12")
				l4d.place(width=yb, height=16, x=otstyp2, y=400)

			if int(bbb) < 0:
				tyu = int(bbb) *(-1)
				tyt = yb - 10
				l3d = Label(text="-", bg=color3, fg=color1, font="Arial 12")
				l3d.place(width=10, height=16, x=otstyp1, y=400)
				l4d = Label(text=tyu, bg=color3, fg=color1, font="Arial 12")
				l4d.place(width=tyt, height=16, x=otstyp2, y=400)

				l5d = Label(text="X", bg=color3, fg=color1, font="Arial 12")
				l5d.place(width=10, height=16, x=otstyp22, y=400)

			if int(bc) > 0:
				l6d = Label(text="+", bg=color3, fg=color1, font="Arial 12")
				l6d.place(width=10, height=16, x=otstyp3, y=400)
				l7d = Label(text=bc, bg=color3, fg=color1, font="Arial 12")
				l7d.place(width=yc, height=16, x=otstyp4, y=400)
					
			if int(bc) < 0:
				tyo = int(bc) *(-1)
				typ = yc - 10
				l6d = Label(text="-", bg=color3, fg=color1, font="Arial 12")
				l6d.place(width=10, height=16, x=otstyp5, y=400)
				l7d = Label(text=tyo, bg=color3, fg=color1, font="Arial 12")
				l7d.place(width=typ, height=16, x=otstyp6, y=400)

			l8d = Label(text="=0", bg=color3, fg=color1, font="Arial 12")
			l8d.place(width=20, height=16, x=otstyp7, y=400)
			l9d = Label(text="D=b²-4ac", bg=color3, fg=color1, font="Arial 12")
			l9d.place(width=65, height=16, x=0, y=420)

			#б в квадрате (топ коммент)
			b22 = int(bbb) ** 2
			ac = int(ba)*int(bc)
			ac4 = int(ac) * 4

			diskr = int(b22) - int(ac4)

			sdis = str(diskr)
			zdiskr = len(sdis)*9

			db20 = str(ac4)
			db2 = len(db20)*9

			l10d = Label(text="D=", bg=color3, fg=color1, font="Arial 12")
			l10d.place(width=18, height=16, x=0, y=440)
			l11d = Label(text=b22, bg=color3, fg=color1, font="Arial 12")
			l11d.place(width=db2, height=16, x=18, y=440)

			otstyp11 = int(db2) + 18
			otstyp12 = otstyp11 + 5

			if int(ac4) >= 0:
				l12d = Label(text="-", bg=color3, fg=color1, font="Arial 12")
				l12d.place(width=5, height=16, x=otstyp11, y=440)
				l13d = Label(text=ac4, bg=color3, fg=color1, font="Arial 12")
				l13d.place(width=db2, height=16, x=otstyp12, y=440)
				
			if int(ac4) < 0:
				l12d = Label(bg=color3)
				l12d.place(width=1, height=1, x=849, y=799)
				l13d = Label(text=ac4, bg=color3, fg=color1, font="Arial 12")
				l13d.place(width=db2, height=16, x=otstyp11, y=440)

			l14d = Label(text="D=", bg=color3, fg=color1, font="Arial 12")
			l14d.place(width=18, height=16, x=0, y=460)
			l15d = Label(text=diskr, bg=color3, fg=color1, font="Arial 12")
			l15d.place(width=zdiskr, height=16, x=18, y=460)

			if diskr > 0:
				import math
				kordsiskr = math.sqrt(int(diskr))
				skord = str(kordsiskr)
				zkord = len(skord)*9

				l16d = Label(text="√D=", bg=color3, fg=color1, font="Arial 12")
				l16d.place(width=26, height=16, x=0, y=480)
				l17d = Label(text=kordsiskr, bg=color3, fg=color1, font="Arial 12")
				l17d.place(width=zkord, height=16, x=26, y=480)

				l18d = Label(text="X₁=-b-√D/2a", bg=color3, fg=color1, font="Arial 12")
				l18d.place(width=92, height=16, x=0, y=500)
				l19d = Label(text="X₂=-b+√D/2a", bg=color3, fg=color1, font="Arial 12")
				l19d.place(width=92, height=16, x=0, y=520)

				l20d = Label(text="X₁=", bg=color3, fg=color1, font="Arial 12")
				l20d.place(width=25, height=16, x=0, y=560)

				znb = int(bbb) * (-1)
				a22 = int(ba) * 2

				zznb = str(znb)
				otstyp21 = len(zznb) * 9

				kkd = str(kordsiskr)
				kd01 = len(kkd)*9

				za2 = str(a22)
				otstyp22 = len(za2) * 9

				otstyp23 = otstyp21 + 25
				otstyp24 = otstyp23 + 5
				otstyp25 = otstyp24 + int(kd01)

				l21d = Label(text=znb, bg=color3, fg=color1, font="Arial 12")
				l21d.place(width=otstyp21, height=16, x=25, y=560)

				a2 = int(ba) * 2

				za2 = str(a2)
				sa2 = len(za2) * 9

				otstyp26 = otstyp25 + 5

				#1

				if kordsiskr > 0:
					l22d = Label(text="-", bg=color3, fg=color1, font="Arial 12")
					l22d.place(width=5, height=16, x=otstyp23, y=560)
					l23d = Label(text=kordsiskr, bg=color3, fg=color1, font="Arial 12")
					l23d.place(width=kd01, height=16, x=otstyp24, y=560)
					l24d = Label(text="/", bg=color3, fg=color1, font="Arial 12")
					l24d.place(width=5, height=16, x=otstyp25, y=560)
					l25d = Label(text=a2, bg=color3, fg=color1, font="Arial 12")
					l25d.place(width=sa2, height=16, x=otstyp26, y=560)

				if kordsiskr < 0:
					l22d = Label(bg=color3)
					l22d.place(width=1, height=1, x=849, y=799)
					l23d = Label(text=kordsiskr, bg=color3, fg=color1, font="Arial 12")
					l23d.place(width=kd01, height=16, x=otstyp23, y=560)
					l24d = Label(text="/", bg=color3, fg=color1, font="Arial 12")
					l24d.place(width=5, height=16, x=otstyp25, y=560)
					l25d = Label(text=a2, bg=color3, fg=color1, font="Arial 12")
					l25d.place(width=sa2, height=16, x=otstyp26, y=560)

				l26d = Label(text="X₂=", bg=color3, fg=color1, font="Arial 12")
				l26d.place(width=25, height=16, x=0, y=580)
				l27d = Label(text=znb, bg=color3, fg=color1, font="Arial 12")
				l27d.place(width=otstyp21, height=16, x=25, y=580)

				#2
				if kordsiskr > 0:
					l28d = Label(text="+", bg=color3, fg=color1, font="Arial 12")
					l28d.place(width=5, height=16, x=otstyp23, y=580)
					l29d = Label(text=kordsiskr, bg=color3, fg=color1, font="Arial 12")
					l29d.place(width=kd01, height=16, x=otstyp24, y=580)
					l30d = Label(text="/", bg=color3, fg=color1, font="Arial 12")
					l30d.place(width=5, height=16, x=otstyp25, y=580)
					l31d = Label(text=a2, bg=color3, fg=color1, font="Arial 12")
					l31d.place(width=sa2, height=16, x=otstyp26, y=580)

				if kordsiskr < 0:
					l28d = Label(bg=color3)
					l28d.place(width=1, height=1, x=849, y=799)
					l29d = Label(text=kordsiskr, bg=color3, fg=color1, font="Arial 12")
					l29d.place(width=kd01, height=16, x=otstyp23, y=580)
					l30d = Label(text="/", bg=color3, fg=color1, font="Arial 12")
					l30d.place(width=5, height=16, x=otstyp25, y=580)
					l31d = Label(text=a2, bg=color3, fg=color1, font="Arial 12")
					l31d.place(width=sa2, height=16, x=otstyp26, y=580)

				l32d = Label(text="X₁=", bg=color3, fg=color1, font="Arial 12")
				l32d.place(width=25, height=16, x=0, y=620)

				znach1 = int(znb) - int(kordsiskr)
				otv1 = int(znach1) / int(a2)

				zotv1 = str(otv1)
				sotv1 = len(zotv1) * 9

				l33d = Label(text=otv1, bg=color3, fg=color1, font="Arial 12")
				l33d.place(width=sotv1, height=16, x=25, y=620)

				l34d = Label(text="X₂=", bg=color3, fg=color1, font="Arial 12")
				l34d.place(width=25, height=16, x=0, y=640)

				znach2 = int(znb) + int(kordsiskr)
				otv2 = int(znach2) / int(a2)

				zotv2 = str(otv2)
				sotv2 = len(zotv2) * 9

				l35d = Label(text=otv2, bg=color3, fg=color1, font="Arial 12")
				l35d.place(width=sotv2, height=16, x=25, y=640)

				l36d = Label(text="Ответ: X=", bg=color3, fg=color1, font="Arial 12")
				l36d.place(width=70, height=16, x=0, y=680)
				l37d = Label(text=otv1, bg=color3, fg=color1, font="Arial 12")
				l37d.place(width=sotv1, height=16, x=70, y=680)

				otstyp31 = int(sotv1) + 70
				otstyp32 = otstyp31 + 5

				l38d = Label(text=";", bg=color3, fg=color1, font="Arial 12")
				l38d.place(width=5, height=16, x=otstyp31, y=680)
				l39d = Label(text=otv2, bg=color3, fg=color1, font="Arial 12")
				l39d.place(width=sotv2, height=16, x=otstyp32, y=680)

			if diskr == 0:
				l16d = Label(text="X=-b/2a", bg=color3, fg=color1, font="Arial 12")
				l16d.place(width=56, height=16, x=0, y=480)
				l17d = Label(text="X=", bg=color3, fg=color1, font="Arial 12")
				l17d.place(width=20, height=16, x=0, y=500)
				
				znb = int(bbb) * (-1)
				a22 = int(ba) * 2

				zznb = str(znb)
				otstyp21 = len(zznb) * 9

				za2 = str(a22)
				otstyp22 = len(za2) * 9
				
				otstyp23 = otstyp21 + 20
				otstyp24 = otstyp23 + 5				

				l18d = Label(text=znb, bg=color3, fg=color1, font="Arial 12")
				l18d.place(width=otstyp21, height=16, x=20, y=500)
				l19d = Label(text="/", bg=color3, fg=color1, font="Arial 12")
				l19d.place(width=5, height=16, x=otstyp23, y=500)
				l20d = Label(text=a22, bg=color3, fg=color1, font="Arial 12")
				l20d.place(width=otstyp22, height=16, x=otstyp24, y=500) 

				l21d = Label(text="X=", bg=color3, fg=color1, font="Arial 12")
				l21d.place(width=20, height=16, x=0, y=520)

				otvet = int(znb) / int(a22)
				zotv = str(otvet)
				sotv = len(zotv) * 9

				l22d = Label(text=otvet, bg=color3, fg=color1, font="Arial 12")
				l22d.place(width=sotv, height=16, x=20, y=520)

				l21d = Label(text="Ответ: X=", bg=color3, fg=color1, font="Arial 12")
				l21d.place(width=70, height=16, x=0, y=540)
				l24d = Label(text=otvet, bg=color3, fg=color1, font="Arial 12")
				l24d.place(width=sotv, height=16, x=70, y=540)

				l25d = Label(bg=color3)
				l25d.place(width=1, height=1, x=849, y=799)
				l26d = Label(bg=color3)
				l26d.place(width=1, height=1, x=849, y=799)
				l27d = Label(bg=color3)
				l27d.place(width=1, height=1, x=849, y=799)
				l28d = Label(bg=color3)
				l28d.place(width=1, height=1, x=849, y=799)
				l29d = Label(bg=color3)
				l29d.place(width=1, height=1, x=849, y=799)
				l30d = Label(bg=color3)
				l30d.place(width=1, height=1, x=849, y=799)
				l31d = Label(bg=color3)
				l31d.place(width=1, height=1, x=849, y=799)
				l32d = Label(bg=color3)
				l32d.place(width=1, height=1, x=849, y=799)
				l33d = Label(bg=color3)
				l33d.place(width=1, height=1, x=849, y=799)
				l34d = Label(bg=color3)
				l34d.place(width=1, height=1, x=849, y=799)
				l35d = Label(bg=color3)
				l35d.place(width=1, height=1, x=849, y=799)
				l36d = Label(bg=color3)
				l36d.place(width=1, height=1, x=849, y=799)
				l37d = Label(bg=color3)
				l37d.place(width=1, height=1, x=849, y=799)
				l38d = Label(bg=color3)
				l38d.place(width=1, height=1, x=849, y=799)
				l39d = Label(bg=color3)
				l39d.place(width=1, height=1, x=849, y=799)

			if diskr < 0:
				l16d = Label(text="Решений нет!", bg=color3, fg=color1, font="Arial 12")
				l16d.place(width=96, height=16, x=0, y=480)	
				l17d = Label(bg=color3)
				l17d.place(width=1, height=1, x=849, y=799)
				l18d = Label(bg=color3)
				l18d.place(width=1, height=1, x=849, y=799)
				l19d = Label(bg=color3)
				l19d.place(width=1, height=1, x=849, y=799)
				l20d = Label(bg=color3)
				l20d.place(width=1, height=1, x=849, y=799)
				l21d = Label(bg=color3)
				l21d.place(width=1, height=1, x=849, y=799)
				l22d = Label(bg=color3)
				l22d.place(width=1, height=1, x=849, y=799)
				l23d = Label(bg=color3)
				l23d.place(width=1, height=1, x=849, y=799)
				l24d = Label(bg=color3)
				l24d.place(width=1, height=1, x=849, y=799)	
				l25d = Label(bg=color3)
				l25d.place(width=1, height=1, x=849, y=799)
				l26d = Label(bg=color3)
				l26d.place(width=1, height=1, x=849, y=799)
				l27d = Label(bg=color3)
				l27d.place(width=1, height=1, x=849, y=799)
				l28d = Label(bg=color3)
				l28d.place(width=1, height=1, x=849, y=799)
				l29d = Label(bg=color3)
				l29d.place(width=1, height=1, x=849, y=799)
				l30d = Label(bg=color3)
				l30d.place(width=1, height=1, x=849, y=799)
				l31d = Label(bg=color3)
				l31d.place(width=1, height=1, x=849, y=799)
				l32d = Label(bg=color3)
				l32d.place(width=1, height=1, x=849, y=799)
				l33d = Label(bg=color3)
				l33d.place(width=1, height=1, x=849, y=799)
				l34d = Label(bg=color3)
				l34d.place(width=1, height=1, x=849, y=799)
				l35d = Label(bg=color3)
				l35d.place(width=1, height=1, x=849, y=799)
				l36d = Label(bg=color3)
				l36d.place(width=1, height=1, x=849, y=799)
				l37d = Label(bg=color3)
				l37d.place(width=1, height=1, x=849, y=799)
				l38d = Label(bg=color3)
				l38d.place(width=1, height=1, x=849, y=799)
				l39d = Label(bg=color3)
				l39d.place(width=1, height=1, x=849, y=799)		

		#Теорема Виета
		#if pr10 == 3 or pr10 == 4:
			#	l1d = Label(text="По теореме Виета:", bg=color3, fg=color1, font="Arial 12")
			#	l1d.place(width=143, height=16, x=0, y=400)
			#	l1d = Label(text="X₁+X₂=-b", bg=color3, fg=color1, font="Arial 12")
			#	l1d.place(width=70, height=16, x=0, y=420)
			#	l1d = Label(text="X₁•X₂=c", bg=color3, fg=color1, font="Arial 12")
			#	l1d.place(width=64, height=16, x=0, y=440)

			#	b22 = int(bbb) ** 2
			#	ac = int(ba)*int(bc)
			#	ac4 = int(ac) * 4
			#	diskr = int(b22) - int(ac4)
			#	import math
			#	kordsiskr = math.sqrt(int(diskr))
			#	znb = int(bbb) * (-1)
			#	a2 = int(ba) * 2
			#	znach1 = int(znb) - int(kordsiskr)
			#	otv1 = int(znach1) / int(a2)
			#	znach2 = int(znb) + int(kordsiskr)
			#	otv2 = int(znach2) / int(a2)

			#	zotv1 = str(otv1)
			#	sotv1 = len(zotv1) * 9

			#	zotv2 = str(otv2)
			#	sotv2 = len(zotv2) * 9

			#	otstyp41 = sotv1 + 5

			#	otstyp42 = otstyp41 + sotv2
			#	otstyp43 = otstyp42 + 5

			#	otstyp44 = otv1 + sotv2
			#	otstyp45 = otstyp44 + 5

			#	l1d = Label(text=otv1, bg=color3, fg=color1, font="Arial 12")
			#	l1d.place(width=sotv1, height=16, x=0, y=480)
				
			#	if otv2 >= 0:
			#		l1d = Label(text="+", bg=color3, fg=color1, font="Arial 12")
			#		l1d.place(width=5, height=16, x=sotv1, y=480)
			#		l1d = Label(text=otv2, bg=color3, fg=color1, font="Arial 12")
			#		l1d.place(width=sotv2, height=16, x=otstyp41, y=480)
			#		l1d = Label(text="=", bg=color3, fg=color1, font="Arial 12")
			#		l1d.place(width=5, height=16, x=otstyp42, y=480)
			#		l1d = Label(text=otv2, bg=color3, fg=color1, font="Arial 12")
			#		l1d.place(width=sotv2, height=16, x=otstyp43, y=480)
				
			#	if otv2 < 0:
			#		l1d = Label(text=otv2, bg=color3, fg=color1, font="Arial 12")
			#		l1d.place(width=sotv2, height=16, x=sotv1, y=480)
			#		l1d = Label(text="=", bg=color3, fg=color1, font="Arial 12")
			#		l1d.place(width=5, height=16, x=otstyp44, y=480)
			#		l1d = Label(text=otv2, bg=color3, fg=color1, font="Arial 12")
			#		l1d.place(width=sotv2, height=16, x=otstyp45, y=480)
			

	except ValueError:
		error = messagebox.showwarning("HIS", "Вы данном поле возможен только ввод цифр, \n все остальные знаки вводить запрещено!")

def v_cv_uy():
	global hh11
	global hh12
	hh11.place_forget()
	hh12.place_forget()
	Lor.place_forget()
	en.place_forget()
	bb.place_forget()
	bb1.place_forget()
	bb2.place_forget()
	h.place_forget()
	f.place_forget()
	l1d.place_forget()
	l2d.place_forget()
	l3d.place_forget()
	l4d.place_forget()
	l5d.place_forget()
	l6d.place_forget()
	l7d.place_forget()
	l8d.place_forget()
	l9d.place_forget()
	l10d.place_forget()
	l11d.place_forget()
	l12d.place_forget()
	l13d.place_forget()
	l14d.place_forget()
	l15d.place_forget()
	l16d.place_forget()
	l17d.place_forget()
	l18d.place_forget()
	#l19d.place_forget()
	#l20d.place_forget()
	#l21d.place_forget()
	#l22d.place_forget()
	#l23d.place_forget()
	#l24d.place_forget()
	#l25d.place_forget()
	#l26d.place_forget()
	#l27d.place_forget()
	#l28d.place_forget()
	#l29d.place_forget()
	#l30d.place_forget()
	#l31d.place_forget()
	#l32d.place_forget()
	#l33d.place_forget()
	#l34d.place_forget()
	#l35d.place_forget()
	#l36d.place_forget()
	#l37d.place_forget()
	#l38d.place_forget()
	#l39d.place_forget()
	# понять, почему это не нужно
	Lh2.place_forget()
	algebra()

def p_cv_uy():
	global l1d
	global l2d
	global l3d
	global l4d
	global l5d
	global l6d
	global l7d
	global l8d
	global l9d
	global l10d
	global l11d
	global l12d
	global l13d
	global l14d
	global l15d
	global l16d
	global l17d
	global l18d
	global l19d
	global l20d
	global l21d
	global l22d
	global l23d
	global l24d
	global l25d
	global l26d
	global l27d
	global l28d
	global l29d
	global l30d
	global l31d
	global l32d
	global l33d
	global l34d
	global l35d
	global l36d
	global l37d
	global l38d
	global l39d
	global Lh2

	l1d.place_forget()
	l2d.place_forget()
	l3d.place_forget()
	l4d.place_forget()
	l5d.place_forget()
	l6d.place_forget()
	l7d.place_forget()
	l8d.place_forget()
	l9d.place_forget()
	l10d.place_forget()
	l11d.place_forget()
	l12d.place_forget()
	l13d.place_forget()
	l14d.place_forget()
	l15d.place_forget()
	l16d.place_forget()
	l17d.place_forget()
	l18d.place_forget()
	l19d.place_forget()
	l20d.place_forget()
	l21d.place_forget()
	l22d.place_forget()
	l23d.place_forget()
	l24d.place_forget()
	l25d.place_forget()
	l26d.place_forget()
	l27d.place_forget()
	l28d.place_forget()
	l29d.place_forget()
	l30d.place_forget()
	l31d.place_forget()
	l32d.place_forget()
	l33d.place_forget()
	l34d.place_forget()
	l35d.place_forget()
	l36d.place_forget()
	l37d.place_forget()
	l38d.place_forget()
	l39d.place_forget()

	Lh2.place_forget()
	h1 = open("files\pomosh\kvad.txt", "r").read()
	Lh2 = Label(text=h1, bg=color3, fg=color2, font="Arial 12")
	Lh2.place(width=850, height=400, x=0, y=400)

# И Н Ф О Р М А Т И К А
# И Н Ф О Р М А Т И К А
# И Н Ф О Р М А Т И К А
# И Н Ф О Р М А Т И К А
# И Н Ф О Р М А Т И К А

def vvod_inf_ss():
	global end
	Lor = Label(image=vss)
	Lor.place(width=850, height=800, x=0, y=0)

	en = Button(image=end, bd=0, command=vibr_pred)
	en.place(width=64, height=49, x=0, y=0)	
	btn1 = Button(text="Кнопка 1", command=perevod_ss) 
	btn1.place(width=268, height=268, x=30, y=173)
	btn2 = Button(text="Кнопка 2") 
	btn2.place(width=315, height=123, x=316, y=173)	
	btn3 = Button(text="Кнопка 3") 
	btn3.place(width=315, height=123, x=316, y=318)
	btn4 = Button(text="Кнопка 4") 
	btn4.place(width=315, height=123, x=316, y=462)
	btn5 = Button(text="Кнопка 5") 
	btn5.place(width=268, height=123, x=30, y=462)

def perevod_ss():
	global sbs
	global iss
	global end
	global s1_listbox
	global s2_listbox
	Lor = Label(image=sss)
	Lor.place(width=850, height=800, x=0, y=0)

	en = Button(image=end, bd=0, command=vvod_inf_ss)
	en.place(width=64, height=49, x=0, y=0)	

	kn25 = Button(text="Двоичная", bg=color3, fg=color, font="Arial 10", command=perepis_21, activebackground=color1, activeforeground=color2, bd=2)
	kn25.place(width=130, height=20, x=360, y=200)
	kn26 = Button(text="Восьмеричная", bg=color3, fg=color, font="Arial 10", command=perepis_22, activebackground=color1, activeforeground=color2, bd=2)
	kn26.place(width=130, height=20, x=360, y=220)
	kn27 = Button(text="Десятичная", bg=color3, fg=color, font="Arial 10", command=perepis_23, activebackground=color1, activeforeground=color2, bd=2)
	kn27.place(width=130, height=20, x=360, y=240)
	kn28 = Button(text="Шестнадцатеричная", bg=color3, fg=color, font="Arial 10", command=perepis_24, activebackground=color1, activeforeground=color2, bd=2)
	kn28.place(width=130, height=20, x=360, y=260)

	sbs = Entry(bg=color3, bd=1, fg=color2, font="Arial 18", width=20)
	sbs.place(width=399, height=35, x=226, y=336)

	h = Button(image=iss, command=resh_ss)
	h.place(width=344, height=54, x=253, y=387)

# 2 - 2
# 8 - 8
# 10 - 1
#16 - 6

def perepis_21():
	global prp
	prp = 2
	l00d = Label(text="2", bg=color3, fg=color, font="Arial 30")
	l00d.place(width=40, height=80, x=500, y=200)
	l01d = Label(text="2", bg=color3, fg=color, font="Arial 30")
	l01d.place(width=40, height=80, x=310, y=200)

def perepis_22():
	global prp
	prp = 8
	l00d = Label(text="8", bg=color3, fg=color, font="Arial 30")
	l00d.place(width=40, height=80, x=500, y=200)
	l01d = Label(text="8", bg=color3, fg=color, font="Arial 30")
	l01d.place(width=40, height=80, x=310, y=200)

def perepis_23():
	global prp
	prp = 1
	l00d = Label(text="10", bg=color3, fg=color, font="Arial 30")
	l00d.place(width=40, height=80, x=500, y=200)
	l01d = Label(text="10", bg=color3, fg=color, font="Arial 30")
	l01d.place(width=40, height=80, x=310, y=200)

def perepis_24():
	global prp
	prp = 6
	l00d = Label(text="16", bg=color3, fg=color, font="Arial 30")
	l00d.place(width=40, height=80, x=500, y=200)
	l01d = Label(text="16", bg=color3, fg=color, font="Arial 30")
	l01d.place(width=40, height=80, x=310, y=200)

def resh_ss():
	try:
		global sbs
		ppr = sbs.get()
		tb1 = int(ppr)
		konz = ""
		global prp
		if prp == 2:
			otv = bin(tb1)
			print(otv)
			l0d = Label(text=otv, bg=color3, fg=color, font="Arial 16")
			l0d.place(width=850, height=40, x=0, y=450)
		if prp == 8:
			otv = oct(tb1)
			print(otv)
		if prp == 1:
			#otv = int([tb1], [2])
			#otv = int([tb1], [8])
			#print(otv)
			print("неа")
		if prp == 6:
			otv = hex(tb1)
			print(otv)
	except ValueError:
		error = messagebox.showwarning("HIS", "Вы данном поле возможен только ввод цифр, \n все остальные знаки вводить запрещено!")
	except NameError:
		error = messagebox.showwarning("HIS", "Выберите системы счисления!")

def shest_res():
	global shest
	dv = shest.get()
	rr = hex(int(dv))
	ld = Label(text=rr, bg="white", fg="black", font="Arial 12")
	ld.place(width=850, height=25, x=0, y=50)

def shest_vv():
	global end
	en = Button(image=end, bd=0, command=informatika)
	en.place(width=64, height=49, x=0, y=0)

	global choice
	choice = 10
	lab = Label(text="Введите число для перевода:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)

	global shest
	shest = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	shest.place(width=500, height=16, x=175, y=70)

	kresh = Button(text="Перевести", background="white", foreground="MediumBluE", font="Arial 16", command=shest_res)
	kresh.place(width=120, height=30, x=362, y=170)
	
	lb = Label(text="Переведённое число:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)

# П Р О С Т Ы Е   В Ы Ч И С Л Е Н И Я
# П Р О С Т Ы Е   В Ы Ч И С Л Е Н И Я
# П Р О С Т Ы Е   В Ы Ч И С Л Е Н И Я
# П Р О С Т Ы Е   В Ы Ч И С Л Е Н И Я
# П Р О С Т Ы Е   В Ы Ч И С Л Е Н И Я
#СЛОЖЕНИЕ
def click(): 
	global vv
	rr = vv.get()
	global vvv
	ff = vvv.get()
	resh = int(rr)+int(ff)
	y1 = len(rr)
	y2 = len(ff)
	y3 = len(str(resh))
	otstyp1 = y1*9
	otstyp2 = y2*9
	otstyp3 = otstyp1+20
	otstyp4 = otstyp3+10
	otstyp5 = otstyp4+otstyp2
	otstyp6 = otstyp5+10
	otstyp7 = y3*9
	l1d = Label(text="1)", bg="white", fg="black", font="Arial 12")
	l1d.place(width=20, height=25, x=0, y=50)
	l2d = Label(text=rr, bg="white", fg="black", font="Arial 12")
	l2d.place(width=otstyp1, height=25, x=20, y=50)
	l3d = Label(text="+", bg="white", fg="black", font="Arial 12")
	l3d.place(width=10, height=25, x=otstyp3, y=50)
	l4d = Label(text=ff, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp2, height=25, x=otstyp4, y=50)
	l5d = Label(text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=10, height=25, x=otstyp5, y=50)
	l6d = Label(text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp7, height=25, x=otstyp6, y=50)
def prost_slog():
	global choice
	choice = 11
	#Первый фрэйм, ввод чисел
	global vv
	vv = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	vv.place(width=100, height=16, x=160, y=44)
	global vvv
	vvv = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	vvv.place(width=100, height=16, x=160, y=64)
	
	#установка первоначальных значений
	
	kresh = Button(text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=click)
	kresh.place(width=120, height=30, x=362, y=170)
#УМНОЖЕНИЕ
def clack(): 
	global qq
	rr = qq.get()
	global qqq
	ff = qqq.get()
	resh = int(rr)*int(ff)
	y1 = len(rr)
	y2 = len(ff)
	y3 = len(str(resh))
	otstyp1 = y1*9
	otstyp2 = y2*9
	otstyp3 = otstyp1+20
	otstyp4 = otstyp3+10
	otstyp5 = otstyp4+otstyp2
	otstyp6 = otstyp5+10
	otstyp7 = y3*9
	l1d = Label(text="1)", bg="white", fg="black", font="Arial 12")
	l1d.place(width=20, height=25, x=0, y=50)
	l2d = Label(text=rr, bg="white", fg="black", font="Arial 12")
	l2d.place(width=otstyp1, height=25, x=20, y=50)
	l3d = Label(text="•", bg="white", fg="black", font="Arial 12")
	l3d.place(width=10, height=25, x=otstyp3, y=50)
	l4d = Label(text=ff, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp2, height=25, x=otstyp4, y=50)
	l5d = Label(text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=10, height=25, x=otstyp5, y=50)
	l6d = Label(text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp7, height=25, x=otstyp6, y=50)
def prost_ymnog():
	global choice
	choice = 13
	#Первый фрэйм, ввод чисел
	global qq
	qq = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	qq.place(width=100, height=16, x=160, y=44)
	global qqq
	qqq = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	qqq.place(width=100, height=16, x=160, y=64)
	
	kresh = Button(text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=clack)
	kresh.place(width=120, height=30, x=362, y=170)
#ДЕЛЕНИЕ
def cleck(): 
	global ww
	rr = ww.get()
	global www
	ff = www.get()
	resh = int(rr)/int(ff)
	y1 = len(rr)
	y2 = len(ff)
	y3 = len(str(resh))
	otstyp1 = y1*9
	otstyp2 = y2*9
	otstyp3 = otstyp1+20
	otstyp4 = otstyp3+10
	otstyp5 = otstyp4+otstyp2
	otstyp6 = otstyp5+10
	otstyp7 = y3*9
	l1d = Label(text="1)", bg="white", fg="black", font="Arial 12")
	l1d.place(width=20, height=25, x=0, y=50)
	l2d = Label(text=rr, bg="white", fg="black", font="Arial 12")
	l2d.place(width=otstyp1, height=25, x=20, y=50)
	l3d = Label(text=":", bg="white", fg="black", font="Arial 12")
	l3d.place(width=10, height=25, x=otstyp3, y=50)
	l4d = Label(text=ff, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp2, height=25, x=otstyp4, y=50)
	l5d = Label(text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=10, height=25, x=otstyp5, y=50)
	l6d = Label(text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp7, height=25, x=otstyp6, y=50)
def prost_del():
	global choice
	choice = 14
	#Первый фрэйм, ввод чисел
	global ww
	ww = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	ww.place(width=100, height=16, x=160, y=44)
	global www
	www = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	www.place(width=100, height=16, x=160, y=64)
	
	kresh = Button(text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=cleck)
	kresh.place(width=120, height=30, x=362, y=170)
#ВЫЧИТАНИЕ
def clock(): 
	global ee
	rr = ee.get()
	global eee
	ff = eee.get()
	resh = int(rr)-int(ff)
	y1 = len(rr)
	y2 = len(ff)
	y3 = len(str(resh))
	otstyp1 = y1*9
	otstyp2 = y2*9
	otstyp3 = otstyp1+20
	otstyp4 = otstyp3+10
	otstyp5 = otstyp4+otstyp2
	otstyp6 = otstyp5+10
	otstyp7 = y3*9
	l1d = Label(text="1)", bg="white", fg="black", font="Arial 12")
	l1d.place(width=20, height=25, x=0, y=50)
	l2d = Label(text=rr, bg="white", fg="black", font="Arial 12")
	l2d.place(width=otstyp1, height=25, x=20, y=50)
	l3d = Label(text="-", bg="white", fg="black", font="Arial 12")
	l3d.place(width=10, height=25, x=otstyp3, y=50)
	l4d = Label(text=ff, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp2, height=25, x=otstyp4, y=50)
	l5d = Label(text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=10, height=25, x=otstyp5, y=50)
	l6d = Label(text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp7, height=25, x=otstyp6, y=50) 
def prost_vichit():
	global choice
	choice = 12
	#Первый фрэйм, ввод чисел
	lab = Label(text="Введите числа:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global ee
	ee = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	ee.place(width=100, height=16, x=160, y=44)
	global eee
	eee = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	eee.place(width=100, height=16, x=160, y=64)
	
	kresh = Button(text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=clock)
	kresh.place(width=120, height=30, x=362, y=170)
#ВОЗВЕДЕНИЕ В СТЕПЕНЬ
def clyck(): 
	global tt
	rr = tt.get()
	global ttt
	ff = ttt.get()
	resh = int(rr)**int(ff)
	l1d = Label(text=resh, bg="white", fg="black", font="Arial 16")
	l1d.place(width=850, height=25, x=0, y=50)
def prost_stepen():
	global choice
	choice = 16
	#Первый фрэйм, ввод чисел
	global tt
	tt = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	tt.place(width=100, height=16, x=110, y=44)
	global ttt
	ttt = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	ttt.place(width=100, height=16, x=110, y=64)
	
	kresh = Button(text="Возвести", background="white", foreground="MediumBluE", font="Arial 16", command=clyck)
	kresh.place(width=200, height=30, x=325, y=170)
#ИЗВЛЕЧЕНИЕ КОРНЯ
def cluck(): 
	global yy
	rr = yy.get()

	import math
	resh = math.sqrt(int(rr))

	l1d = Label(text=resh, bg="white", fg="black", font="Arial 16")
	l1d.place(width=850, height=25, x=0, y=50)
def prost_koren():
	global choice
	choice = 15
	#Первый фрэйм, ввод чисел
	global yy
	yy = Entry( bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	yy.place(width=100, height=16, x=110, y=44)
	
	kresh = Button(text="Извлечь", background="white", foreground="MediumBluE", font="Arial 16", command=cluck)
	kresh.place(width=200, height=30, x=325, y=170)

# Х И М И Я
# Х И М И Я
# Х И М И Я
# Х И М И Я
# Х И М И Я 

def v_harakter():
	global Lh
	global en
	global Lor1

	global Icd
	global Icd0

	Icd.place_forget()
	Icd0.place_forget()

	Lor1.place_forget()

	en.place_forget()

	global l0b
	global l1b
	global l2b
	global l3b
	global l4b
	global l5b
	global l6b
	global l7b
	global l8b
	global l9b
	global l10b
	global l11b
	global l12b
	global l13b
	global l14b
	global l15b
	global lob
	global lcb
	global lab

	l0b.place_forget()
	l1b.place_forget()
	l2b.place_forget()
	l3b.place_forget()
	l4b.place_forget()
	l5b.place_forget()
	l6b.place_forget()
	l7b.place_forget()
	l8b.place_forget()
	l9b.place_forget()
	l10b.place_forget()
	l11b.place_forget()
	l12b.place_forget()
	l13b.place_forget()
	l14b.place_forget()
	l15b.place_forget()
	lob.place_forget()
	lcb.place_forget()
	lab.place_forget()

	global H_checkbutton
	global Hh_checkbutton
	global He_checkbutton
	global Li_checkbutton
	global Be_checkbutton
	global B_checkbutton
	global C_checkbutton
	global N_checkbutton
	global O_checkbutton
	global F_checkbutton
	global Ne_checkbutton
	global Na_checkbutton
	global Mg_checkbutton
	global Al_checkbutton
	global Si_checkbutton
	global P_checkbutton
	global S_checkbutton
	global Cl_checkbutton
	global Ar_checkbutton
	global K_checkbutton
	global Ca_checkbutton
	global Sc_checkbutton
	global Ti_checkbutton
	global V_checkbutton
	global Cr_checkbutton
	global Mn_checkbutton
	global Fe_checkbutton
	global Co_checkbutton
	global Ni_checkbutton
	global Cu_checkbutton
	global Zn_checkbutton
	global Ga_checkbutton
	global Ge_checkbutton
	global As_checkbutton
	global Se_checkbutton
	global Br_checkbutton
	global Kr_checkbutton
	global Rb_checkbutton
	global Sr_checkbutton
	global Y_checkbutton
	global Zr_checkbutton
	global Nb_checkbutton
	global Mo_checkbutton
	global Tc_checkbutton
	global Ru_checkbutton
	global Rh_checkbutton
	global Pd_checkbutton
	global Ag_checkbutton
	global Cd_checkbutton
	global In_checkbutton
	global Sn_checkbutton
	global Sb_checkbutton
	global Te_checkbutton
	global I_checkbutton
	global Xe_checkbutton
	global Cs_checkbutton
	global Ba_checkbutton
	global La_checkbutton
	global Hf_checkbutton
	global Ta_checkbutton
	global W_checkbutton
	global Re_checkbutton
	global Os_checkbutton
	global Ir_checkbutton
	global Pt_checkbutton
	global Au_checkbutton
	global Hg_checkbutton
	global Tl_checkbutton
	global Pb_checkbutton
	global Bi_checkbutton
	global Po_checkbutton
	global At_checkbutton
	global Rn_checkbutton
	global Fr_checkbutton
	global Ra_checkbutton
	global Ac_checkbutton
	global Rf_checkbutton
	global Db_checkbutton
	global Sg_checkbutton
	global Bh_checkbutton
	global Hs_checkbutton
	global Mt_checkbutton
	global Ds_checkbutton
	global Ce_checkbutton
	global Pr_checkbutton
	global Nd_checkbutton
	global Pm_checkbutton
	global Sm_checkbutton
	global Eu_checkbutton
	global Gd_checkbutton
	global Tb_checkbutton
	global Dy_checkbutton
	global Ho_checkbutton
	global Er_checkbutton
	global Tm_checkbutton
	global Yb_checkbutton
	global Lu_checkbutton
	global Th_checkbutton
	global Pa_checkbutton
	global U_checkbutton
	global Np_checkbutton
	global Pu_checkbutton
	global Am_checkbutton
	global Cm_checkbutton
	global Bk_checkbutton
	global Cf_checkbutton
	global Es_checkbutton
	global Fm_checkbutton
	global Md_checkbutton
	global No_checkbutton
	global Lr_checkbutton

	Lh.place_forget()

	H_checkbutton.place_forget()
	Hh_checkbutton.place_forget()
	H_checkbutton.place_forget()
	Hh_checkbutton.place_forget()
	He_checkbutton.place_forget()
	Li_checkbutton.place_forget()
	Be_checkbutton.place_forget()
	B_checkbutton.place_forget()
	C_checkbutton.place_forget()
	N_checkbutton.place_forget()
	O_checkbutton.place_forget()
	F_checkbutton.place_forget()
	Ne_checkbutton.place_forget()
	Na_checkbutton.place_forget()
	Mg_checkbutton.place_forget()
	Al_checkbutton.place_forget()
	Si_checkbutton.place_forget()
	P_checkbutton.place_forget()
	S_checkbutton.place_forget()
	Cl_checkbutton.place_forget()
	Ar_checkbutton.place_forget()
	K_checkbutton.place_forget()
	Ca_checkbutton.place_forget()
	Sc_checkbutton.place_forget()
	Ti_checkbutton.place_forget()
	V_checkbutton.place_forget()
	Cr_checkbutton.place_forget()
	Mn_checkbutton.place_forget()
	Fe_checkbutton.place_forget()
	Co_checkbutton.place_forget()
	Ni_checkbutton.place_forget()
	Cu_checkbutton.place_forget()
	Zn_checkbutton.place_forget()
	Ga_checkbutton.place_forget()
	Ge_checkbutton.place_forget()
	As_checkbutton.place_forget()
	Se_checkbutton.place_forget()
	Br_checkbutton.place_forget()
	Kr_checkbutton.place_forget()
	Rb_checkbutton.place_forget()
	Sr_checkbutton.place_forget()
	Y_checkbutton.place_forget()
	Zr_checkbutton.place_forget()
	Nb_checkbutton.place_forget()
	Mo_checkbutton.place_forget()
	Tc_checkbutton.place_forget()
	Ru_checkbutton.place_forget()
	Rh_checkbutton.place_forget()
	Pd_checkbutton.place_forget()
	Ag_checkbutton.place_forget()
	Cd_checkbutton.place_forget()
	In_checkbutton.place_forget()
	Sn_checkbutton.place_forget()
	Sb_checkbutton.place_forget()
	Te_checkbutton.place_forget()
	I_checkbutton.place_forget()
	Xe_checkbutton.place_forget()
	Cs_checkbutton.place_forget()
	Ba_checkbutton.place_forget()
	La_checkbutton.place_forget()
	Hf_checkbutton.place_forget()
	Ta_checkbutton.place_forget()
	W_checkbutton.place_forget()
	Re_checkbutton.place_forget()
	Os_checkbutton.place_forget()
	Ir_checkbutton.place_forget()
	Pt_checkbutton.place_forget()
	Au_checkbutton.place_forget()
	Hg_checkbutton.place_forget()
	Tl_checkbutton.place_forget()
	Pb_checkbutton.place_forget()
	Bi_checkbutton.place_forget()
	Po_checkbutton.place_forget()
	At_checkbutton.place_forget()
	Rn_checkbutton.place_forget()
	Fr_checkbutton.place_forget()
	Ra_checkbutton.place_forget()
	Ac_checkbutton.place_forget()
	Rf_checkbutton.place_forget()
	Db_checkbutton.place_forget()
	Sg_checkbutton.place_forget()
	Bh_checkbutton.place_forget()
	Hs_checkbutton.place_forget()
	Mt_checkbutton.place_forget()
	Ds_checkbutton.place_forget()
	Ce_checkbutton.place_forget()
	Pr_checkbutton.place_forget()
	Nd_checkbutton.place_forget()
	Pm_checkbutton.place_forget()
	Sm_checkbutton.place_forget()
	Eu_checkbutton.place_forget()
	Gd_checkbutton.place_forget()
	Tb_checkbutton.place_forget()
	Dy_checkbutton.place_forget()
	Ho_checkbutton.place_forget()
	Er_checkbutton.place_forget()
	Tm_checkbutton.place_forget()
	Yb_checkbutton.place_forget()
	Lu_checkbutton.place_forget()
	Th_checkbutton.place_forget()
	Pa_checkbutton.place_forget()
	U_checkbutton.place_forget()
	Np_checkbutton.place_forget()
	Pu_checkbutton.place_forget()
	Am_checkbutton.place_forget()
	Cm_checkbutton.place_forget()
	Bk_checkbutton.place_forget()
	Cf_checkbutton.place_forget()
	Es_checkbutton.place_forget()
	Fm_checkbutton.place_forget()
	Md_checkbutton.place_forget()
	No_checkbutton.place_forget()
	Lr_checkbutton.place_forget()
	himia()

def harakter():
	global Lh
	global en

	lt.place_forget()
	ent.place_forget()
	nht.place_forget()

	global l0b
	global l1b
	global l2b
	global l3b
	global l4b
	global l5b
	global l6b
	global l7b
	global l8b
	global l9b
	global l10b
	global l11b
	global l12b
	global l13b
	global l14b
	global l15b
	global lob
	global lcb
	global lab

	global Icd
	global Icd0

	global H_checkbutton
	global Hh_checkbutton
	global He_checkbutton
	global Li_checkbutton
	global Be_checkbutton
	global B_checkbutton
	global C_checkbutton
	global N_checkbutton
	global O_checkbutton
	global F_checkbutton
	global Ne_checkbutton
	global Na_checkbutton
	global Mg_checkbutton
	global Al_checkbutton
	global Si_checkbutton
	global P_checkbutton
	global S_checkbutton
	global Cl_checkbutton
	global Ar_checkbutton
	global K_checkbutton
	global Ca_checkbutton
	global Sc_checkbutton
	global Ti_checkbutton
	global V_checkbutton
	global Cr_checkbutton
	global Mn_checkbutton
	global Fe_checkbutton
	global Co_checkbutton
	global Ni_checkbutton
	global Cu_checkbutton
	global Zn_checkbutton
	global Ga_checkbutton
	global Ge_checkbutton
	global As_checkbutton
	global Se_checkbutton
	global Br_checkbutton
	global Kr_checkbutton
	global Rb_checkbutton
	global Sr_checkbutton
	global Y_checkbutton
	global Zr_checkbutton
	global Nb_checkbutton
	global Mo_checkbutton
	global Tc_checkbutton
	global Ru_checkbutton
	global Rh_checkbutton
	global Pd_checkbutton
	global Ag_checkbutton
	global Cd_checkbutton
	global In_checkbutton
	global Sn_checkbutton
	global Sb_checkbutton
	global Te_checkbutton
	global I_checkbutton
	global Xe_checkbutton
	global He_checkbutton
	global Cs_checkbutton
	global Ba_checkbutton
	global La_checkbutton
	global Hf_checkbutton
	global Ta_checkbutton
	global W_checkbutton
	global Re_checkbutton
	global Os_checkbutton
	global Ir_checkbutton
	global Pt_checkbutton
	global Au_checkbutton
	global Hg_checkbutton
	global Tl_checkbutton
	global Pb_checkbutton
	global Bi_checkbutton
	global Po_checkbutton
	global At_checkbutton
	global Rn_checkbutton
	global Fr_checkbutton
	global Ra_checkbutton
	global Ac_checkbutton
	global Rf_checkbutton
	global Db_checkbutton
	global Sg_checkbutton
	global Bh_checkbutton
	global Hs_checkbutton
	global Mt_checkbutton
	global Ds_checkbutton
	global Ce_checkbutton
	global Pr_checkbutton
	global Nd_checkbutton
	global Pm_checkbutton
	global Sm_checkbutton
	global Eu_checkbutton
	global Gd_checkbutton
	global Tb_checkbutton
	global Dy_checkbutton
	global Ho_checkbutton
	global Er_checkbutton
	global Tm_checkbutton
	global Yb_checkbutton
	global Lu_checkbutton
	global Th_checkbutton
	global Pa_checkbutton
	global U_checkbutton
	global Np_checkbutton
	global Pu_checkbutton
	global Am_checkbutton
	global Cm_checkbutton
	global Bk_checkbutton
	global Cf_checkbutton
	global Es_checkbutton
	global Fm_checkbutton
	global Md_checkbutton
	global No_checkbutton
	global Lr_checkbutton

	global Lor1

	Lor1 = Label(image=tmh)
	Lor1.place(width=850, height=800, x=0, y=0)
	en = Button(image=end, bd=0, command=v_harakter)
	en.place(width=64, height=49, x=0, y=0)
	Lh = Label(bg=color3)
	Lh.place(width=1, height=1, x=849, y=799)
	
	lab = Label(text="Выберите элемент:", bg=color3, fg=color1, font="Arial 16")
	lab.place(width=200, height=25, x=64, y=0)
	#ряд
	l1b = Label(text="1", bg=color3, fg=color, font="Arial 18")
	l1b.place(width=64, height=25, x=0, y=49)
	l2b = Label(text="2", bg=color3, fg=color, font="Arial 18")
	l2b.place(width=64, height=25, x=0, y=74)
	l3b = Label(text="3", bg=color3, fg=color, font="Arial 18")
	l3b.place(width=64, height=25, x=0, y=99)
	l4b = Label(text="4", bg=color3, fg=color, font="Arial 18")
	l4b.place(width=64, height=25, x=0, y=124)
	l5b = Label(text="5", bg=color3, fg=color, font="Arial 18")
	l5b.place(width=64, height=25, x=0, y=149)
	l6b = Label(text="6", bg=color3, fg=color, font="Arial 18")
	l6b.place(width=64, height=25, x=0, y=174)
	l7b = Label(text="7", bg=color3, fg=color, font="Arial 18")
	l7b.place(width=64, height=25, x=0, y=199)
	l0b = Label(text="8", bg=color3, fg=color, font="Arial 18")
	l0b.place(width=64, height=25, x=0, y=224)
	lob = Label(text="9", bg=color3, fg=color, font="Arial 18")
	lob.place(width=64, height=25, x=0, y=249)
	lcb = Label(text="10", bg=color3, fg=color, font="Arial 18")
	lcb.place(width=64, height=25, x=0, y=274)
	#группы
	l8b = Label(text="I", bg=color3, fg=color, font="Arial 18")
	l8b.place(width=50, height=24, x=64, y=25)
	l9b = Label(text="II", bg=color3, fg=color, font="Arial 18")
	l9b.place(width=50, height=24, x=114, y=25)
	l10b = Label(text="III", bg=color3, fg=color, font="Arial 18")
	l10b.place(width=50, height=24, x=164, y=25)
	l11b = Label(text="IV", bg=color3, fg=color, font="Arial 18")
	l11b.place(width=50, height=24, x=214, y=25)
	l12b = Label(text="V", bg=color3, fg=color, font="Arial 18")
	l12b.place(width=50, height=24, x=264, y=25)
	l13b = Label(text="VI", bg=color3, fg=color, font="Arial 18")
	l13b.place(width=50, height=24, x=314, y=25)
	l14b = Label(text="VII", bg=color3, fg=color, font="Arial 18")
	l14b.place(width=50, height=24, x=364, y=25)
	l15b = Label(text="VIII", bg=color3, fg=color, font="Arial 18")
	l15b.place(width=50, height=24, x=414, y=25)
	
	H_checkbutton = Button(text="H", bg="#00CD00", font="Arial 12", bd=0, command=H_check, fg=color3, activebackground=color, activeforeground=color3)
	H_checkbutton.place(width=48, height=23, x=65, y=50)
	
	Hh_checkbutton = Button(text="H", bg="#00CD00", font="Arial 12", bd=0, command=Hh_check, fg=color3, activebackground=color, activeforeground=color3)
	Hh_checkbutton.place(width=48, height=23, x=365, y=50)

	He_checkbutton = Button(text="He", bg="#5A00FF", font="Arial 12", bd=0, command=He_check, fg=color3, activebackground=color, activeforeground=color3)
	He_checkbutton.place(width=48, height=23, x=415, y=50)
	# 2 ряд
	Li_checkbutton = Button(text="Li", bg="#00CD00", font="Arial 12", bd=0, command=Li_check, fg=color3, activebackground=color, activeforeground=color3)
	Li_checkbutton.place(width=48, height=23, x=65, y=75)

	Be_checkbutton = Button(text="Be", bg="#00CD00", font="Arial 12", bd=0, command=Be_check, fg=color3, activebackground=color, activeforeground=color3)
	Be_checkbutton.place(width=48, height=23, x=115, y=75)

	B_checkbutton = Button(text="B", bg="#FEE910", font="Arial 12", bd=0, command=B_check, fg=color3, activebackground=color, activeforeground=color3)
	B_checkbutton.place(width=48, height=23, x=165, y=75)

	C_checkbutton = Button(text="C", bg="#FEE910", font="Arial 12", bd=0, command=C_check, fg=color3, activebackground=color, activeforeground=color3)
	C_checkbutton.place(width=48, height=23, x=215, y=75)

	N_checkbutton = Button(text="N", bg="#FEE910", font="Arial 12", bd=0, command=N_check, fg=color3, activebackground=color, activeforeground=color3)
	N_checkbutton.place(width=48, height=23, x=265, y=75)

	O_checkbutton = Button(text="O", bg="#FEE910", font="Arial 12", bd=0, command=O_check, fg=color3, activebackground=color, activeforeground=color3)
	O_checkbutton.place(width=48, height=23, x=315, y=75)

	F_checkbutton = Button(text="N", bg="#FEE910", font="Arial 12", bd=0, command=F_check, fg=color3, activebackground=color, activeforeground=color3)
	F_checkbutton.place(width=48, height=23, x=365, y=75)

	Ne_checkbutton = Button(text="Ne", bg="#5A00FF", font="Arial 12", bd=0, command=Ne_check, fg=color3, activebackground=color, activeforeground=color3)
	Ne_checkbutton.place(width=48, height=23, x=415, y=75)
	# 3 ряд
	Na_checkbutton = Button(text="Na", bg="#00CD00", font="Arial 12", bd=0, command=Na_check, fg=color3, activebackground=color, activeforeground=color3)
	Na_checkbutton.place(width=48, height=23, x=65, y=100)

	Mg_checkbutton = Button(text="Mg", bg="#00CD00", font="Arial 12", bd=0, command=Mg_check, fg=color3, activebackground=color, activeforeground=color3)
	Mg_checkbutton.place(width=48, height=23, x=115, y=100)

	Al_checkbutton = Button(text="Al", bg="#CD00CD", font="Arial 12", bd=0, command=Al_check, fg=color3, activebackground=color, activeforeground=color3)
	Al_checkbutton.place(width=48, height=23, x=165, y=100)

	Si_checkbutton = Button(text="Si", bg="#FEE910", font="Arial 12", bd=0, command=Si_check, fg=color3, activebackground=color, activeforeground=color3)
	Si_checkbutton.place(width=48, height=23, x=215, y=100)

	P_checkbutton = Button(text="P", bg="#FEE910", font="Arial 12", bd=0, command=P_check, fg=color3, activebackground=color, activeforeground=color3)
	P_checkbutton.place(width=48, height=23, x=265, y=100)

	S_checkbutton = Button(text="S", bg="#FEE910", font="Arial 12", bd=0, command=S_check, fg=color3, activebackground=color, activeforeground=color3)
	S_checkbutton.place(width=48, height=23, x=315, y=100)

	Cl_checkbutton = Button(text="Cl", bg="#FEE910", font="Arial 12", bd=0, command=Cl_check, fg=color3, activebackground=color, activeforeground=color3)
	Cl_checkbutton.place(width=48, height=23, x=365, y=100)

	Ar_checkbutton = Button(text="Ar", bg="#5A00FF", font="Arial 12", bd=0, command=Ar_check, fg=color3, activebackground=color, activeforeground=color3)
	Ar_checkbutton.place(width=48, height=23, x=415, y=100)
	# 4 ряд
	K_checkbutton = Button(text="K", bg="#00CD00", font="Arial 12", bd=0, command=K_check, fg=color3, activebackground=color, activeforeground=color3)
	K_checkbutton.place(width=48, height=23, x=65, y=125)

	Ca_checkbutton = Button(text="Ca", bg="#00CD00", font="Arial 12", bd=0, command=Ca_check, fg=color3, activebackground=color, activeforeground=color3)
	Ca_checkbutton.place(width=48, height=23, x=115, y=125)

	Sc_checkbutton = Button(text="Sc", bg="#00CD00", font="Arial 12", bd=0, command=Sc_check, fg=color3, activebackground=color, activeforeground=color3)
	Sc_checkbutton.place(width=48, height=23, x=165, y=125)
	
	Ti_checkbutton = Button(text="Ti", bg="#00CD00", font="Arial 12", bd=0, command=Ti_check, fg=color3, activebackground=color, activeforeground=color3)
	Ti_checkbutton.place(width=48, height=23, x=215, y=125)

	V_checkbutton = Button(text="V", bg="#00CD00", font="Arial 12", bd=0, command=V_check, fg=color3, activebackground=color, activeforeground=color3)
	V_checkbutton.place(width=48, height=23, x=265, y=125)

	Cr_checkbutton = Button(text="Cr", bg="#00CD00", font="Arial 12", bd=0, command=Cr_check, fg=color3, activebackground=color, activeforeground=color3)
	Cr_checkbutton.place(width=48, height=23, x=315, y=125)

	Mn_checkbutton = Button(text="Mn", bg="#00CD00", font="Arial 12", bd=0, command=Mn_check, fg=color3, activebackground=color, activeforeground=color3)
	Mn_checkbutton.place(width=48, height=23, x=365, y=125)

	Fe_checkbutton = Button(text="Fe", bg="#00CD00", font="Arial 12", bd=0, command=Fe_check, fg=color3, activebackground=color, activeforeground=color3)
	Fe_checkbutton.place(width=48, height=23, x=415, y=125)

	Co_checkbutton = Button(text="Co", bg="#00CD00", font="Arial 12", bd=0, command=Co_check, fg=color3, activebackground=color, activeforeground=color3)
	Co_checkbutton.place(width=48, height=23, x=465, y=125)

	Ni_checkbutton = Button(text="Ni", bg="#00CD00", font="Arial 12", bd=0, command=Ni_check, fg=color3, activebackground=color, activeforeground=color3)
	Ni_checkbutton.place(width=48, height=23, x=515, y=125)
	# 5 ряд
	Cu_checkbutton = Button(text="Cu", bg="#00CD00", font="Arial 12", bd=0, command=Cu_check, fg=color3, activebackground=color, activeforeground=color3)
	Cu_checkbutton.place(width=48, height=23, x=65, y=150)

	Zn_checkbutton = Button(text="Zn", bg="#00CD00", font="Arial 12", bd=0, command=Zn_check, fg=color3, activebackground=color, activeforeground=color3)
	Zn_checkbutton.place(width=48, height=23, x=115, y=150)

	Ga_checkbutton = Button(text="Ga", bg="#00CD00", font="Arial 12", bd=0, command=Ga_check, fg=color3, activebackground=color, activeforeground=color3)
	Ga_checkbutton.place(width=48, height=23, x=165, y=150)

	Ge_checkbutton = Button(text="Ge", bg="#CD00CD", font="Arial 12", bd=0, command=Ge_check, fg=color3, activebackground=color, activeforeground=color3)
	Ge_checkbutton.place(width=48, height=23, x=215, y=150)

	As_checkbutton = Button(text="As", bg="#FEE910", font="Arial 12", bd=0, command=As_check, fg=color3, activebackground=color, activeforeground=color3)
	As_checkbutton.place(width=48, height=23, x=265, y=150)

	Se_checkbutton = Button(text="Se", bg="#FEE910", font="Arial 12", bd=0, command=Se_check, fg=color3, activebackground=color, activeforeground=color3)
	Se_checkbutton.place(width=48, height=23, x=315, y=150)

	Br_checkbutton = Button(text="Br", bg="#FEE910", font="Arial 12", bd=0, command=Br_check, fg=color3, activebackground=color, activeforeground=color3)
	Br_checkbutton.place(width=48, height=23, x=365, y=150)

	Kr_checkbutton = Button(text="Kr", bg="#5A00FF", font="Arial 12", bd=0, command=Kr_check, fg=color3, activebackground=color, activeforeground=color3)
	Kr_checkbutton.place(width=48, height=23, x=415, y=150)
	# 6 ряд
	Rb_checkbutton = Button(text="Rb", bg="#00CD00", font="Arial 12", bd=0, command=Rb_check, fg=color3, activebackground=color, activeforeground=color3)
	Rb_checkbutton.place(width=48, height=23, x=65, y=175)

	Sr_checkbutton = Button(text="Sr", bg="#00CD00", font="Arial 12", bd=0, command=Sr_check, fg=color3, activebackground=color, activeforeground=color3)
	Sr_checkbutton.place(width=48, height=23, x=115, y=175)

	Y_checkbutton = Button(text="Y", bg="#00CD00", font="Arial 12", bd=0, command=Y_check, fg=color3, activebackground=color, activeforeground=color3)
	Y_checkbutton.place(width=48, height=23, x=165, y=175)

	Zr_checkbutton = Button(text="Zr", bg="#00CD00", font="Arial 12", bd=0, command=Zr_check, fg=color3, activebackground=color, activeforeground=color3)
	Zr_checkbutton.place(width=48, height=23, x=215, y=175)

	Nb_checkbutton = Button(text="Nb", bg="#00CD00", font="Arial 12", bd=0, command=Nb_check, fg=color3, activebackground=color, activeforeground=color3)
	Nb_checkbutton.place(width=48, height=23, x=265, y=175)

	Mo_checkbutton = Button(text="Mo", bg="#00CD00", font="Arial 12", bd=0, command=Mo_check, fg=color3, activebackground=color, activeforeground=color3)
	Mo_checkbutton.place(width=48, height=23, x=315, y=175)

	Tc_checkbutton = Button(text="Tc", bg="#00CD00", font="Arial 12", bd=0, command=Tc_check, fg=color3, activebackground=color, activeforeground=color3)
	Tc_checkbutton.place(width=48, height=23, x=365, y=175)

	Ru_checkbutton = Button(text="Ru", bg="#00CD00", font="Arial 12", bd=0, command=Ru_check, fg=color3, activebackground=color, activeforeground=color3)
	Ru_checkbutton.place(width=48, height=23, x=415, y=175)

	Rh_checkbutton = Button(text="Rh", bg="#00CD00", font="Arial 12", bd=0, command=Rh_check, fg=color3, activebackground=color, activeforeground=color3)
	Rh_checkbutton.place(width=48, height=23, x=465, y=175)

	Pd_checkbutton = Button(text="Pd", bg="#00CD00", font="Arial 12", bd=0, command=Pd_check, fg=color3, activebackground=color, activeforeground=color3)
	Pd_checkbutton.place(width=48, height=23, x=515, y=175)
	# 7 ряд
	Ag_checkbutton = Button(text="Ag", bg="#00CD00", font="Arial 12", bd=0, command=Ag_check, fg=color3, activebackground=color, activeforeground=color3)
	Ag_checkbutton.place(width=48, height=23, x=65, y=200)

	Cd_checkbutton = Button(text="Cd", bg="#00CD00", font="Arial 12", bd=0, command=Cd_check, fg=color3, activebackground=color, activeforeground=color3)
	Cd_checkbutton.place(width=48, height=23, x=115, y=200)

	In_checkbutton = Button(text="In", bg="#CD00CD", font="Arial 12", bd=0, command=In_check, fg=color3, activebackground=color, activeforeground=color3)
	In_checkbutton.place(width=48, height=23, x=165, y=200)

	Sn_checkbutton = Button(text="Sn", bg="#CD00CD", font="Arial 12", bd=0, command=Sn_check, fg=color3, activebackground=color, activeforeground=color3)
	Sn_checkbutton.place(width=48, height=23, x=215, y=200)

	Sb_checkbutton = Button(text="In", bg="#CD00CD", font="Arial 12", bd=0, command=Sb_check, fg=color3, activebackground=color, activeforeground=color3)
	Sb_checkbutton.place(width=48, height=23, x=265, y=200)

	Te_checkbutton = Button(text="Te", bg="#FEE910", font="Arial 12", bd=0, command=Te_check, fg=color3, activebackground=color, activeforeground=color3)
	Te_checkbutton.place(width=48, height=23, x=315, y=200)

	I_checkbutton = Button(text="I", bg="#FEE910", font="Arial 12", bd=0, command=I_check, fg=color3, activebackground=color, activeforeground=color3)
	I_checkbutton.place(width=48, height=23, x=365, y=200)

	Xe_checkbutton = Button(text="Xe", bg="#5A00FF", font="Arial 12", bd=0, command=Xe_check, fg=color3, activebackground=color, activeforeground=color3)
	Xe_checkbutton.place(width=48, height=23, x=415, y=200)
	# 8 ряд
	Cs_checkbutton = Button(text="Cs", bg="#00CD00", font="Arial 12", bd=0, command=Cs_check, fg=color3, activebackground=color, activeforeground=color3)
	Cs_checkbutton.place(width=48, height=23, x=65, y=225)

	Ba_checkbutton = Button(text="Ba", bg="#00CD00", font="Arial 12", bd=0, command=Ba_check, fg=color3, activebackground=color, activeforeground=color3)
	Ba_checkbutton.place(width=48, height=23, x=115, y=225)
	# Лантан
	La_checkbutton = Button(text="La'", bg="#00CD00", font="Arial 12", bd=0, command=La_check, fg=color3, activebackground=color, activeforeground=color3)
	La_checkbutton.place(width=48, height=23, x=165, y=225)

	Hf_checkbutton = Button(text="Hf", bg="#00CD00", font="Arial 12", bd=0, command=Hf_check, fg=color3, activebackground=color, activeforeground=color3)
	Hf_checkbutton.place(width=48, height=23, x=215, y=225)

	Ta_checkbutton = Button(text="Ta", bg="#00CD00", font="Arial 12", bd=0, command=Ta_check, fg=color3, activebackground=color, activeforeground=color3)
	Ta_checkbutton.place(width=48, height=23, x=265, y=225)

	W_checkbutton = Button(text="W", bg="#00CD00", font="Arial 12", bd=0, command=W_check, fg=color3, activebackground=color, activeforeground=color3)
	W_checkbutton.place(width=48, height=23, x=315, y=225)

	Re_checkbutton = Button(text="Re", bg="#00CD00", font="Arial 12", bd=0, command=Re_check, fg=color3, activebackground=color, activeforeground=color3)
	Re_checkbutton.place(width=48, height=23, x=365, y=225)

	Os_checkbutton = Button(text="Os", bg="#00CD00", font="Arial 12", bd=0, command=Os_check, fg=color3, activebackground=color, activeforeground=color3)
	Os_checkbutton.place(width=48, height=23, x=415, y=225)

	Ir_checkbutton = Button(text="Ir", bg="#00CD00", font="Arial 12", bd=0, command=Ir_check, fg=color3, activebackground=color, activeforeground=color3)
	Ir_checkbutton.place(width=48, height=23, x=465, y=225)

	Pt_checkbutton = Button(text="Pt", bg="#00CD00", font="Arial 12", bd=0, command=Pt_check, fg=color3, activebackground=color, activeforeground=color3)
	Pt_checkbutton.place(width=48, height=23, x=515, y=225)
	# 9 ряд
	Au_checkbutton = Button(text="Au", bg="#00CD00", font="Arial 12", bd=0, command=Au_check, fg=color3, activebackground=color, activeforeground=color3)
	Au_checkbutton.place(width=48, height=23, x=65, y=250)

	Hg_checkbutton = Button(text="Hg", bg="#00CD00", font="Arial 12", bd=0, command=Hg_check, fg=color3, activebackground=color, activeforeground=color3)
	Hg_checkbutton.place(width=48, height=23, x=115, y=250)
	
	Tl_checkbutton = Button(text="Tl", bg="#00CD00", font="Arial 12", bd=0, command=Ti_check, fg=color3, activebackground=color, activeforeground=color3)
	Tl_checkbutton.place(width=48, height=23, x=165, y=250)

	Pb_checkbutton = Button(text="Pb", bg="#00CD00", font="Arial 12", bd=0, command=Pb_check, fg=color3, activebackground=color, activeforeground=color3)
	Pb_checkbutton.place(width=48, height=23, x=215, y=250)

	Bi_checkbutton = Button(text="Bi", bg="#CD00CD", font="Arial 12", bd=0, command=Bi_check, fg=color3, activebackground=color, activeforeground=color3)
	Bi_checkbutton.place(width=48, height=23, x=265, y=250)

	Po_checkbutton = Button(text="Po", bg="#CD00CD", font="Arial 12", bd=0, command=Po_check, fg=color3, activebackground=color, activeforeground=color3)
	Po_checkbutton.place(width=48, height=23, x=315, y=250)

	At_checkbutton = Button(text="At", bg="#CD00CD", font="Arial 12", bd=0, command=At_check, fg=color3, activebackground=color, activeforeground=color3)
	At_checkbutton.place(width=48, height=23, x=365, y=250)

	Rn_checkbutton = Button(text="Rn", bg="#5A00FF", font="Arial 12", bd=0, command=Rn_check, fg=color3, activebackground=color, activeforeground=color3)
	Rn_checkbutton.place(width=48, height=23, x=415, y=250)
	# 10 ряд
	Fr_checkbutton = Button(text="Fr", bg="#00CD00", font="Arial 12", bd=0, command=Fr_check, fg=color3, activebackground=color, activeforeground=color3)
	Fr_checkbutton.place(width=48, height=23, x=65, y=275)

	Ra_checkbutton = Button(text="Ra", bg="#00CD00", font="Arial 12", bd=0, command=Ra_check, fg=color3, activebackground=color, activeforeground=color3)
	Ra_checkbutton.place(width=48, height=23, x=115, y=275)
	# Актиний
	Ac_checkbutton = Button(text="Ac'", bg="#00CD00", font="Arial 12", bd=0, command=Ac_check, fg=color3, activebackground=color, activeforeground=color3)
	Ac_checkbutton.place(width=48, height=23, x=165, y=275)

	Rf_checkbutton = Button(text="Rf", bg="#00CD00", font="Arial 12", bd=0, command=Rf_check, fg=color3, activebackground=color, activeforeground=color3)
	Rf_checkbutton.place(width=48, height=23, x=215, y=275)

	Db_checkbutton = Button(text="Db", bg="#00CD00", font="Arial 12", bd=0, command=Db_check, fg=color3, activebackground=color, activeforeground=color3)
	Db_checkbutton.place(width=48, height=23, x=265, y=275)

	Sg_checkbutton = Button(text="Sg", bg="#00CD00", font="Arial 12", bd=0, command=Sg_check, fg=color3, activebackground=color, activeforeground=color3)
	Sg_checkbutton.place(width=48, height=23, x=315, y=275)

	Bh_checkbutton = Button(text="Bh", bg="#00CD00", font="Arial 12", bd=0, command=Bh_check, fg=color3, activebackground=color, activeforeground=color3)
	Bh_checkbutton.place(width=48, height=23, x=365, y=275)

	Hs_checkbutton = Button(text="Hs", bg="#00CD00", font="Arial 12", bd=0, command=Hs_check, fg=color3, activebackground=color, activeforeground=color3)
	Hs_checkbutton.place(width=48, height=23, x=415, y=275)

	Mt_checkbutton = Button(text="Mt", bg="#00CD00", font="Arial 12", bd=0, command=Mt_check, fg=color3, activebackground=color, activeforeground=color3)
	Mt_checkbutton.place(width=48, height=23, x=465, y=275)

	Ds_checkbutton = Button(text="Ds", bg="#00CD00", font="Arial 12", bd=0, command=Ds_check, fg=color3, activebackground=color, activeforeground=color3)
	Ds_checkbutton.place(width=48, height=23, x=515 , y=275)

	#Лантаноиды
	Icd = Label(text="Лантаноиды", bg=color3, fg=color, font="Arial 12")
	Icd.place(width=100, height=20, x=600, y=30)

	Ce_checkbutton = Button(text="Ce", bg="#FFBF00", font="Arial 12", bd=0, command=Ce_check, fg=color3, activebackground=color, activeforeground=color3)
	Ce_checkbutton.place(width=48, height=23, x=601, y=50)

	Pr_checkbutton = Button(text="Pr", bg="#FFBF00", font="Arial 12", bd=0, command=Pr_check, fg=color3, activebackground=color, activeforeground=color3)
	Pr_checkbutton.place(width=48, height=23, x=601, y=75)

	Nd_checkbutton = Button(text="Nd", bg="#FFBF00", font="Arial 12", bd=0, command=Nd_check, fg=color3, activebackground=color, activeforeground=color3)
	Nd_checkbutton.place(width=48, height=23, x=601, y=100)

	Pm_checkbutton = Button(text="Pm", bg="#FFBF00", font="Arial 12", bd=0, command=Pm_check, fg=color3, activebackground=color, activeforeground=color3)
	Pm_checkbutton.place(width=48, height=23, x=601, y=125)

	Sm_checkbutton = Button(text="Sm", bg="#FFBF00", font="Arial 12", bd=0, command=Sm_check, fg=color3, activebackground=color, activeforeground=color3)
	Sm_checkbutton.place(width=48, height=23, x=601, y=150)

	Eu_checkbutton = Button(text="Eu", bg="#FFBF00", font="Arial 12", bd=0, command=Eu_check, fg=color3, activebackground=color, activeforeground=color3)
	Eu_checkbutton.place(width=48, height=23, x=601, y=175)

	Gd_checkbutton = Button(text="Gd", bg="#FFBF00", font="Arial 12", bd=0, command=Gd_check, fg=color3, activebackground=color, activeforeground=color3)
	Gd_checkbutton.place(width=48, height=23, x=601, y=200)
	#
	Tb_checkbutton = Button(text="Tb", bg="#FFBF00", font="Arial 12", bd=0, command=Tb_check, fg=color3, activebackground=color, activeforeground=color3)
	Tb_checkbutton.place(width=48, height=23, x=651, y=50)

	Dy_checkbutton = Button(text="Dy", bg="#FFBF00", font="Arial 12", bd=0, command=Dy_check, fg=color3, activebackground=color, activeforeground=color3)
	Dy_checkbutton.place(width=48, height=23, x=651, y=75)

	Ho_checkbutton = Button(text="Ho", bg="#FFBF00", font="Arial 12", bd=0, command=Ho_check, fg=color3, activebackground=color, activeforeground=color3)
	Ho_checkbutton.place(width=48, height=23, x=651, y=100)

	Er_checkbutton = Button(text="Er", bg="#FFBF00", font="Arial 12", bd=0, command=Er_check, fg=color3, activebackground=color, activeforeground=color3)
	Er_checkbutton.place(width=48, height=23, x=651, y=125)

	Tm_checkbutton = Button(text="Tm", bg="#FFBF00", font="Arial 12", bd=0, command=Tm_check, fg=color3, activebackground=color, activeforeground=color3)
	Tm_checkbutton.place(width=48, height=23, x=651, y=150)

	Yb_checkbutton = Button(text="Yb", bg="#FFBF00", font="Arial 12", bd=0, command=Yb_check, fg=color3, activebackground=color, activeforeground=color3)
	Yb_checkbutton.place(width=48, height=23, x=651, y=175)

	Lu_checkbutton = Button(text="Lu", bg="#FFBF00", font="Arial 12", bd=0, command=Lu_check, fg=color3, activebackground=color, activeforeground=color3)
	Lu_checkbutton.place(width=48, height=23, x=651, y=200)

	#Актиноиды
	Icd0 = Label(text="Актиноиды", bg=color3, fg=color, font="Arial 12")
	Icd0.place(width=100, height=20, x=750, y=30)

	Th_checkbutton = Button(text="Th", bg="#FFBF00", font="Arial 12", bd=0, command=Th_check, fg=color3, activebackground=color, activeforeground=color3)
	Th_checkbutton.place(width=48, height=23, x=751, y=50)

	Pa_checkbutton = Button(text="Pa", bg="#FFBF00", font="Arial 12", bd=0, command=Pa_check, fg=color3, activebackground=color, activeforeground=color3)
	Pa_checkbutton.place(width=48, height=23, x=751, y=75)

	U_checkbutton = Button(text="U", bg="#FFBF00", font="Arial 12", bd=0, command=U_check, fg=color3, activebackground=color, activeforeground=color3)
	U_checkbutton.place(width=48, height=23, x=751, y=100)

	Np_checkbutton = Button(text="Np", bg="#FFBF00", font="Arial 12", bd=0, command=Np_check, fg=color3, activebackground=color, activeforeground=color3)
	Np_checkbutton.place(width=48, height=23, x=751, y=125)

	Pu_checkbutton = Button(text="Pu", bg="#FFBF00", font="Arial 12", bd=0, command=Pu_check, fg=color3, activebackground=color, activeforeground=color3)
	Pu_checkbutton.place(width=48, height=23, x=751, y=150)

	Am_checkbutton = Button(text="Am", bg="#FFBF00", font="Arial 12", bd=0, command=Am_check, fg=color3, activebackground=color, activeforeground=color3)
	Am_checkbutton.place(width=48, height=23, x=751, y=175)

	Cm_checkbutton = Button(text="Cm", bg="#FFBF00", font="Arial 12", bd=0, command=Cm_check, fg=color3, activebackground=color, activeforeground=color3)
	Cm_checkbutton.place(width=48, height=23, x=751, y=200)
	#
	Bk_checkbutton = Button(text="Bk", bg="#FFBF00", font="Arial 12", bd=0, command=Bk_check, fg=color3, activebackground=color, activeforeground=color3)
	Bk_checkbutton.place(width=48, height=23, x=801, y=50)

	Cf_checkbutton = Button(text="Cf", bg="#FFBF00", font="Arial 12", bd=0, command=Cf_check, fg=color3, activebackground=color, activeforeground=color3)
	Cf_checkbutton.place(width=48, height=23, x=801, y=75)

	Es_checkbutton = Button(text="Es", bg="#FFBF00", font="Arial 12", bd=0, command=Es_check, fg=color3, activebackground=color, activeforeground=color3)
	Es_checkbutton.place(width=48, height=23, x=801, y=100)

	Fm_checkbutton = Button(text="Fm", bg="#FFBF00", font="Arial 12", bd=0, command=Fm_check, fg=color3, activebackground=color, activeforeground=color3)
	Fm_checkbutton.place(width=48, height=23, x=801, y=125)

	Md_checkbutton = Button(text="Md", bg="#FFBF00", font="Arial 12", bd=0, command=Md_check, fg=color3, activebackground=color, activeforeground=color3)
	Md_checkbutton.place(width=48, height=23, x=801, y=150)

	No_checkbutton = Button(text="No", bg="#FFBF00", font="Arial 12", bd=0, command=No_check, fg=color3, activebackground=color, activeforeground=color3)
	No_checkbutton.place(width=48, height=23, x=801, y=175)

	Lr_checkbutton = Button(text="Lr", bg="#FFBF00", font="Arial 12", bd=0, command=Lr_check, fg=color3, activebackground=color, activeforeground=color3)
	Lr_checkbutton.place(width=48, height=23, x=801, y=200)

def H_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter\H.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Hh_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter\H.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def He_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter\He.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Li_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter\Li.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Be_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter\Be.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def B_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter\B.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def C_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter\C.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def N_check():
	global Lh
	Lh.place_forget()
	h_h = open ("files\harakter/N.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def O_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter\O.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def F_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter\F.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ne_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ne.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Na_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Na.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Mg_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Mg.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Al_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Al.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Si_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Si.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def P_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/P.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def S_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/S.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Cl_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Cl.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ar_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ar.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def K_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/K.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ca_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ca.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Sc_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Sc.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ti_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ti.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def V_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/V.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Cr_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Cr.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Mn_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Mn.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Fe_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Fe.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Co_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Co.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ni_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ni.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Cu_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Cu.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Zn_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Zn.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ga_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ga.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ge_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ge.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def As_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/As.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Se_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Se.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Br_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Br.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Kr_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Kr.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Rb_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Rb.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Sr_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Sr.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Y_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Y.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Zr_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Zr.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Nb_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Nb.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Mo_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Mo.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Tc_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Tc.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ru_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ru.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Rh_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Rh.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Pd_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Pd.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ag_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ag.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Cd_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Cd.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def In_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/In.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Sn_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Sn.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Sb_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Sb.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Te_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Te.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def I_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/I.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Xe_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Xe.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Cs_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Cs.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ba_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ba.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def La_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/La.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Hf_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Hf.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ta_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ta.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def W_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/W.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Re_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Re.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Os_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Os.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ir_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ir.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Pt_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Pt.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Au_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Au.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Hg_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Hg.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Tl_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Tl.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Pb_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Pb.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Bi_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Bi.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Po_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Po.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def At_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/At.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Fr_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Fr.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ra_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ra.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ac_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ac.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Rf_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Rf.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Db_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Db.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Sg_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Sg.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Bh_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Bh.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Hs_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Hs.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Mt_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Mt.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ds_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ds.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Rn_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Rn.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ce_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ce.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Pr_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Pr.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Nd_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Nd.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Pm_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Pm.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Sm_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Sm.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Eu_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Eu.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Gd_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Gd.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Tb_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Tb.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Dy_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Dy.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Ho_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Ho.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Er_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Er.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Tm_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Tm.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Yb_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Yb.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Lu_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Lu.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Th_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Th.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Pa_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Pa.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def U_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/U.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Np_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Np.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Pu_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Pu.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Am_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Am.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Cm_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Cm.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Bk_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Bk.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Cf_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Cf.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Es_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Es.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Fm_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Fm.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Md_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Md.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def No_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/No.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)
def Lr_check():
	global Lh
	Lh.place_forget()
	h_h = open("files\harakter/Lr.txt", "r").read()
	Lh = Label(text=h_h, bg=color3, fg=color, font="Arial 16")
	Lh.place(width=560, height=420, x=0, y=300)

# Ф О Р М У Л Ы
# Ф О Р М У Л Ы
# Ф О Р М У Л Ы
# Ф О Р М У Л Ы
# Ф О Р М У Л Ы

def visov_formul():
	global lq
	global en
	global nh0
	global nh1
	global nh2
	global nh3
	global nh4
	global nh5
	lq.place_forget()
	en.place_forget()
	nh0.place_forget()
	nh1.place_forget()
	nh2.place_forget()
	nh3.place_forget()
	nh4.place_forget()
	nh5.place_forget()

	global mm
	global Lor
	global ma
	global mg
	global mf
	global mh
	global enq
	Lor = Label(image=pm)
	Lor.place(width=850, height=800, x=0, y=0)
	mm = Button(image=pmm, bd=0, command=ff_mat)
	mm.place(width=427, height=90, x=211.5, y=144)
	ma = Button(image=pma, bd=0, command=ff_alg)
	ma.place(width=427, height=90, x=211.5, y=274)
	mg = Button(image=pmg, bd=0, command=ff_geo)
	mg.place(width=427, height=90, x=211.5, y=404)
	mf = Button(image=pmf, bd=0, command=ff_fiz)
	mf.place(width=427, height=90, x=211.5, y=534)
	mh = Button(image=pmh, bd=0, command=ff_him)
	mh.place(width=427, height=90, x=211.5, y=664)
	enq = Button(image=end, bd=0, command=v_ff)
	enq.place(width=64, height=49, x=0, y=0)

def v_ff():
	global Lor
	global mm
	global ma
	global mg
	global mf
	global mh
	global enq
	Lor.place_forget()
	mm.place_forget()
	ma.place_forget()
	mg.place_forget()
	mf.place_forget()
	mh.place_forget()
	enq.place_forget()
	vibr_pred()

def ff_him():
	global Lor
	global mm
	global ma
	global mg
	global mf
	global mh
	global enq
	Lor.place_forget()
	mm.place_forget()
	ma.place_forget()
	mg.place_forget()
	mf.place_forget()
	mh.place_forget()
	enq.place_forget()

	global ff_hi

	Lor = Label(image=ff_hi)

def ff_geo():
	global Lor
	global mm
	global ma
	global mg
	global mf
	global mh
	global enq
	Lor.place_forget()
	mm.place_forget()
	ma.place_forget()
	mg.place_forget()
	mf.place_forget()
	mh.place_forget()
	enq.place_forget()

	global ff_ge

	Lor = Label(image=ff_ge)

def ff_fiz():
	global Lor
	global mm
	global ma
	global mg
	global mf
	global mh
	global enq
	Lor.place_forget()
	mm.place_forget()
	ma.place_forget()
	mg.place_forget()
	mf.place_forget()
	mh.place_forget()
	enq.place_forget()

	global ff_fi

	Lor = Label(image=ff_fi)

def ff_mat():
	global Lor
	global mm
	global ma
	global mg
	global mf
	global mh
	global enq
	Lor.place_forget()
	mm.place_forget()
	ma.place_forget()
	mg.place_forget()
	mf.place_forget()
	mh.place_forget()
	enq.place_forget()

	global ff_ma
	global maf1
	global maf2
	global maf3
	global maf4
	global maf5
	global maf6
	global maf7
	global maf8
	global maf9

	Lor = Label(image=ff_ma)
	Lor.place(width=850, height=800, x=0, y=0)

	fb = Button(image=maf1, bd=0)#, command=)
	fb.place(width=169, height=99, x=455, y=504)
	fb = Button(image=maf2, bd=0)#, command=)
	fb.place(width=169, height=99, x=652, y=504)
	fb = Button(image=maf3, bd=0)#, command=)
	fb.place(width=169, height=99, x=652, y=652)
	fb = Button(image=maf4, bd=0)#, command=)
	fb.place(width=169, height=99, x=227, y=504)
	fb = Button(image=maf5, bd=0)#, command=)
	fb.place(width=169, height=99, x=30, y=504)
	fb = Button(image=maf6, bd=0)#, command=)
	fb.place(width=169, height=99, x=30, y=652)
	fb = Button(image=maf7, bd=0)#, command=)
	fb.place(width=366, height=99, x=30, y=80)
	fb = Button(image=maf8, bd=0)#, command=)
	fb.place(width=397, height=99, x=227, y=652)
	fb = Button(image=maf9, bd=0)#, command=)
	fb.place(width=366, height=99, x=455, y=80)

def ff_alg():
	global Lor
	global mm
	global ma
	global mg
	global mf
	global mh
	global enq
	Lor.place_forget()
	mm.place_forget()
	ma.place_forget()
	mg.place_forget()
	mf.place_forget()
	mh.place_forget()
	enq.place_forget()

	global ff_alg

	Lor = Label(image=ff_alg)

root.mainloop()
