
Reverse Engineering Tables
==========================

``AIDLL.dll``
-------------

.. table::

   ============= ========== ================ =======
   Function Name Address    Relative Address Ordinal
   ============= ========== ================ =======
   ``deinitDll`` 0x10024630 0x00024630       1 (0x1)
   ``initDll``   0x100241d0 0x000241d0       2 (0x2)
   ============= ========== ================ =======

``AIDLL_w32ded.dll``
--------------------

.. table::

   ============= ========== ================ =======
   Function Name Address    Relative Address Ordinal
   ============= ========== ================ =======
   ``deinitDll`` 0x100637e0 0x100637e0       1 (0x1)
   ``initDll``   0x10063340 0x00063340       2 (0x2)
   ============= ========== ================ =======

``BF2Audio.dll``
----------------

.. table::

   ======================= ========== ================ =======
   Function Name           Address    Relative Address Ordinal
   ======================= ========== ================ =======
   ``getSoundEngine``      0x10007ad0 0x00007ad0       1 (0x1)
   ``shutdownSoundEngine`` 0x10007b80 0x00007b80       2 (0x2)
   ======================= ========== ================ =======

``BF2OpenAL.dll``
-----------------

.. table::

   ========================== ========== ================ =========
   Function Name              Address    Relative Address Ordinal
   ========================== ========== ================ =========
   ``alBuffer3f``             0x100092a0 0x000092a0       3 (0x3)
   ``alBuffer3i``             0x100092a0 0x000092a0       4 (0x4)
   ``alBufferData``           0x10008700 0x00008700       5 (0x5)
   ``alBufferf``              0x100092a0 0x000092a0       6 (0x6)
   ``alBufferfv``             0x100092a0 0x000092a0       7 (0x7)
   ``alBufferi``              0x100092a0 0x000092a0       8 (0x8)
   ``alBufferiv``             0x100092a0 0x000092a0       9 (0x9)
   ``alcCaptureCloseDevice``  0x1002f260 0x0002f260       76 (0x4c)
   ``alcCaptureOpenDevice``   0x10030c00 0x00030c00       77 (0x4d)
   ``alcCaptureSamples``      0x1002f3d0 0x0002f3d0       78 (0x4e)
   ``alcCaptureStart``        0x1002f370 0x0002f370       79 (0x4f)
   ``alcCaptureStop``         0x1002f3a0 0x0002f3a0       80 (0x50)
   ``alcCloseDevice``         0x1002f9e0 0x0002f9e0       81 (0x51)
   ``alcCreateContext``       0x100360c0 0x000360c0       82 (0x52)
   ``alcDestroyContext``      0x1002f840 0x0002f840       83 (0x53)
   ``alcGetContextsDevice``   0x1002f900 0x0002f900       84 (0x54)
   ``alcGetCurrentContext``   0x1002f8d0 0x0002f8d0       85 (0x55)
   ``alcGetEnumValue``        0x1002f810 0x0002f810       86 (0x56)
   ``alcGetError``            0x1002f6c0 0x0002f6c0       87 (0x57)
   ``alcGetIntegerv``         0x10031010 0x00031010       88 (0x58)
   ``alcGetProcAddress``      0x1002f790 0x0002f790       89 (0x59)
   ``alcGetString``           0x100331e0 0x000331e0       90 (0x5a)
   ``alcIsExtensionPresent``  0x1002f6e0 0x0002f6e0       91 (0x5b)
   ``alcMakeContextCurrent``  0x1002f950 0x0002f950       92 (0x5c)
   ``alcOpenDevice``          0x10033490 0x00033490       93 (0x5d)
   ``alcProcessContext``      0x1002f6d0 0x0002f6d0       94 (0x5e)
   ``alcSuspendContext``      0x1002f6d0 0x0002f6d0       95 (0x5f)
   ``alDeleteBuffers``        0x10009680 0x00009680       10 (0xa)
   ``alDeleteSources``        0x1001c450 0x0001c450       11 (0xb)
   ``alDisable``              0x1001e930 0x0001e930       12 (0xc)
   ``alDistanceModel``        0x1001f350 0x0001f350       13 (0xd)
   ``alDopplerFactor``        0x1001f170 0x0001f170       14 (0xe)
   ``alDopplerVelocity``      0x1001f210 0x0001f210       15 (0xf)
   ``alEnable``               0x1001e930 0x0001e930       16 (0x10)
   ``alGenBuffers``           0x10008570 0x00008570       17 (0x11)
   ``alGenSources``           0x1001c110 0x0001c110       18 (0x12)
   ``alGetBoolean``           0x1001e9b0 0x0001e9b0       19 (0x13)
   ``alGetBooleanv``          0x1001ed40 0x0001ed40       20 (0x14)
   ``alGetBuffer3f``          0x10009500 0x00009500       21 (0x15)
   ``alGetBuffer3i``          0x10009500 0x00009500       22 (0x16)
   ``alGetBufferf``           0x10009300 0x00009300       23 (0x17)
   ``alGetBufferfv``          0x10009300 0x00009300       24 (0x18)
   ``alGetBufferi``           0x10009380 0x00009380       25 (0x19)
   ``alGetBufferiv``          0x10009590 0x00009590       26 (0x1a)
   ``alGetDouble``            0x1001eaa0 0x0001eaa0       27 (0x1b)
   ``alGetDoublev``           0x1001ee30 0x0001ee30       28 (0x1c)
   ``alGetEnumValue``         0x10018ca0 0x00018ca0       29 (0x1d)
   ``alGetError``             0x10018aa0 0x00018aa0       30 (0x1e)
   ``alGetFloat``             0x1001eb90 0x0001eb90       31 (0x1f)
   ``alGetFloatv``            0x1001ef00 0x0001ef00       32 (0x20)
   ``alGetInteger``           0x1001ec70 0x0001ec70       33 (0x21)
   ``alGetIntegerv``          0x1001efd0 0x0001efd0       34 (0x22)
   ``alGetListener3f``        0x10019460 0x00019460       35 (0x23)
   ``alGetListener3i``        0x100196a0 0x000196a0       36 (0x24)
   ``alGetListenerf``         0x100193c0 0x000193c0       37 (0x25)
   ``alGetListenerfv``        0x10019510 0x00019510       38 (0x26)
   ``alGetListeneri``         0x10019630 0x00019630       39 (0x27)
   ``alGetListeneriv``        0x10019780 0x00019780       40 (0x28)
   ``alGetProcAddress``       0x10018c40 0x00018c40       41 (0x29)
   ``alGetSource3f``          0x10019f20 0x00019f20       42 (0x2a)
   ``alGetSource3i``          0x10019ff0 0x00019ff0       43 (0x2b)
   ``alGetSourcef``           0x1001c600 0x0001c600       44 (0x2c)
   ``alGetSourcefv``          0x1001c8f0 0x0001c8f0       45 (0x2d)
   ``alGetSourcei``           0x1001ca50 0x0001ca50       46 (0x2e)
   ``alGetSourceiv``          0x1001cd80 0x0001cd80       47 (0x2f)
   ``alGetString``            0x1001f0b0 0x0001f0b0       48 (0x30)
   ``alIsBuffer``             0x100086a0 0x000086a0       49 (0x31)
   ``alIsEnabled``            0x1001e970 0x0001e970       50 (0x32)
   ``alIsExtensionPresent``   0x10018b20 0x00018b20       51 (0x33)
   ``alIsSource``             0x100198c0 0x000198c0       52 (0x34)
   ``alListener3f``           0x10018e10 0x00018e10       53 (0x35)
   ``alListener3i``           0x10019200 0x00019200       54 (0x36)
   ``alListenerf``            0x10018d00 0x00018d00       55 (0x37)
   ``alListenerfv``           0x10018f40 0x00018f40       56 (0x38)
   ``alListeneri``            0x10019190 0x00019190       57 (0x39)
   ``alListeneriv``           0x10019280 0x00019280       58 (0x3a)
   ``alSource3f``             0x10019940 0x00019940       59 (0x3b)
   ``alSource3i``             0x10019b70 0x00019b70       60 (0x3c)
   ``alSourcef``              0x1001d2f0 0x0001d2f0       71 (0x47)
   ``alSourcefv``             0x1001da90 0x0001da90       72 (0x48)
   ``alSourcei``              0x1001dc00 0x0001dc00       73 (0x49)
   ``alSourceiv``             0x1001e530 0x0001e530       74 (0x4a)
   ``alSourcePause``          0x1001a100 0x0001a100       61 (0x3d)
   ``alSourcePausev``         0x1001a190 0x0001a190       62 (0x3e)
   ``alSourcePlay``           0x1001e670 0x0001e670       63 (0x3f)
   ``alSourcePlayv``          0x1001e7b0 0x0001e7b0       64 (0x40)
   ``alSourceQueueBuffers``   0x1001cf60 0x0001cf60       65 (0x41)
   ``alSourceRewind``         0x1001a440 0x0001a440       66 (0x42)
   ``alSourceRewindv``        0x1001a500 0x0001a500       67 (0x43)
   ``alSourceStop``           0x1001a270 0x0001a270       68 (0x44)
   ``alSourceStopv``          0x1001a330 0x0001a330       69 (0x45)
   ``alSourceUnqueueBuffers`` 0x1001a620 0x0001a620       70 (0x46)
   ``alSpeedOfSound``         0x1001f2b0 0x0001f2b0       75 (0x4b)
   ``EAXGet``                 0x1000b7d0 0x0000b7d0       1 (0x1)
   ``EAXSet``                 0x1000ba90 0x0000ba90       2 (0x2)
   ========================== ========== ================ =========

``BF2VoipServer.dll``
---------------------

.. list-table::
   :header-rows: 1

   * - ``Function Name``
     - Address
     - Relative Address
     - Ordinal
   * - ``public: __thiscall BF2VoipServer::CBF2VoipServer::CBF2VoipServer(void)``
     - 0x10001380
     - 0x00001380
     - 1 (0x1)
   * - ``public: __thiscall BF2VoipServer::CBF2VoipServer::~CBF2VoipServer(void)``
     - 0x100013d0
     - 0x000013d0
     - 2 (0x2)
   * - ``public: bool __thiscall BF2VoipServer::CBF2VoipServer::IsRunning(void)``
     - 0x100011a0
     - 0x000011a0
     - 5 (0x5)
   * - ``public: class BF2VoipServer::CBF2VoipServerInstance* __thiscall BF2VoipServer::CBF2VoipServer::getInstance(unsigned int)``
     - 0x100012a0
     - 0x000012a0
     - 10 (0xa)
   * - ``public: enum VOIP::VRESULT __thiscall BF2VoipServer::CBF2VoipServer::CreateInstance(unsigned int,class std::basic_string<char,struct std::char_traits,class std::allocator >,int &)``
     - 0x10001680
     - 0x00001680
     - 3 (0x3)
   * - ``public: enum VOIP::VRESULT __thiscall BF2VoipServer::CBF2VoipServer::Initialize(bool)``
     - 0x100011b0
     - 0x000011b0
     - 4 (0x4)
   * - ``public: enum VOIP::VRESULT __thiscall BF2VoipServer::CBF2VoipServer::ReleaseAllInstances(void)``
     - 0x10001500
     - 0x00001500
     - 6 (0x6)
   * - ``public: enum VOIP::VRESULT __thiscall BF2VoipServer::CBF2VoipServer::ReleaseInstance(int)``
     - 0x10001450
     - 0x00001450
     - 7 (0x7)
   * - ``public: enum VOIP::VRESULT __thiscall BF2VoipServer::CBF2VoipServer::Shutdown(void)``
     - 0x100015d0
     - 0x000015d0
     - 8 (0x8)
   * - ``public: enum VOIP::VRESULT __thiscall BF2VoipServer::CBF2VoipServer::Update(void)``
     - 0x100012d0
     - 0x000012d0
     - 9 (0x9)
   * - ``public: unsigned int __thiscall BF2VoipServer::CBF2VoipServer::getNumInstances(void)``
     - 0x10001280
     - 0x00001280
     - 11 (0xb)
