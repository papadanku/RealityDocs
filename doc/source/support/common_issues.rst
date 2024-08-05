
Common Issues
=============

RendDX9 Error
-------------

Intel Core
   PCs or Laptops with a Discrete GPU
      #. Navigate :menuselection:`Windows Settings --> Graphics Settings`
      #. Switch ``prbf2.exe`` to run on the :guilabel:`Discrete GPU`

   PCs or Laptops with no Discrete GPU
      Update your Intel Xe/ARC Graphics driver.

      :download:`https://www.intel.com/content/www/us/en/download/785597/intel-arc-iris-xe-graphics-windows.html`
   
   .. warning::

      Issue prevalent on the following
         - Intel Core 11th gen and newer
         - Intel N100 and other N-series
         - Pentium G7xxx series
         - Intel ARC Alchemist dGPUs

``memory.dll`` Crashes After Play Sessions
------------------------------------------

Happens due to some unknown differences in the way GPU drivers allocate memory, hence why some players might not encounter this error at all

Experimental Fix
   Use DXVK and enable the config ``d3d9.deviceLossOnFocusLoss = True``. DXVK has a built in mapped memory, making longer session less prone to crashes but there are still some bugs with DXVK hence why this is marked as experimental.

   :download:`https://github.com/doitsujin/dxvk`

Cannot Hear Anything
--------------------

- Disable positional audio inside Mumble's settings

   Might work, might not

- Plug your headphone via the included USB cable
- Buy a backup wired audio for PR purposes

   I personally recommend cheap Chinese in-ear monitors for PR

Performance Slowly Degrades Overtime
------------------------------------

- Your PC might need a thorough cleaning and a repaste
- Set a more aggressive fan curve to keep CPU turbo clocks high

Low Performance on Ryzen CPUs
-----------------------------

#. Enable :guilabel:`CPPC` and :guilabel:`CPPC`\-preferred cores.
#. Enable :guilabel:`CPB` (Core Performance Boost) and :guilabel:`PBO`

#. :menuselection:`BIOS' advanced menu --> AMD CBS --> Zen/CPU common options menu`
#. Enable the following:

   - :guilabel:`L1` & :guilabel:`L2` Cache Hardware Prefetcher
   - :guilabel:`Streaming Stores Control`
   - :guilabel:`OPcache Control`

Launched Into an Infinite Black Screen
--------------------------------------

- Make sure that there's no 3rd party antivirus that's blocking PR
- Launch PR with an offline profile, if it works then something is wrong with your network, try a VPN or consult to your ISP

Stuck on "Joining Server"
-------------------------

Stems from multiple possible issues:
   Network issue on player's end
      - Switch to wired ethernet
      - Try a VPN
      - Complain to your ISP

   PR is placed on an external drive, that's not formatted in NTFS
      Reformat your drive to NTFS or place it back to your internal drive

Persistent Skipping/Stuttering
------------------------------

Possible Solutions:
   - Switch to wired ethernet
   - Switch to a newer WiFi protocol that has a higher frequency

      Make sure your router and PC/laptop supports it!

If you can't do either of those
   - Make sure that your WiFi is at least on a less-crowded channel
   - Increase your transmit power
