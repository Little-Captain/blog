Title: Building C++ Applications
Date: 2017-10-19 16:18:14
Category: C++
Tags: C++

> 编译、链接、打包
> 可执行程序、静态库、动态库
> 构建、工具集

# 编译、链接、打包、可执行程序、静态库、动态库

* The three basic tools used to build C++ applications are the `compiler`, the `linker`, and the `archiver` (or librarian). A collection of these programs and possibly other tools is called a toolset.
    * The `compiler` takes C++ source files as input and produces `object files`, which `contain` a mixture of `machine-executable code` and `symbolic references to functions and data`. 
    * The `archiver` takes a collection of `object files` as `input` and `produces a static library`, or archive, `which is simply a collection of object files grouped for convenient use`. 
    * The `linker` takes a collection of `object files` and `libraries` and `resolves` their `symbolic references` to `produce` either an `executable` or `dynamic library`. Roughly speaking, the `linker` operates by `matching each use of a symbol to its definition`. When an executable or dynamic library is created, it is said to be linked; the libraries used to build the executable or dynamic library are said to be linked against.
* An `executable`, or application, is simply any program that can be executed by the operating system. 
* A `dynamic library`, also called a `shared library`, is like an executable except that `it can’t be run on its own`; `it consists of a body of machine-executable code that is loaded into memory after an application is started and can be shared by one or more applications.` On Windows, dynamic libraries are also called dynamic link libraries (DLLs).
* The `object files` and `static libraries` on which an executable depends are needed only when the executable is built. 
* The `dynamic libraries` on which an executable depends, however, must be present on a user’s system when the executable is run.

**File extensions on Windows and Unix**

| File type | Windows | Mac OS X | Other Unix |
| :-: | :-: | :-: | :-: |
| Object files | .obj | .o | .o |
| Static libraries | .lib | .a | .a |
| Dynamic libraries | .dll | .dylib | .so |
| Executables | .exe | No extension | No extension |

# 构建、工具集

## 构建

* A `build system` provides a text file format for describing a collection of source files and the binary files that should be generated from them, together with a build tool that reads these text files and generates the binary files by invoking the appropriate command-line tools. Typically, these text files are created and edited using a text editor, and the build tool is invoked from the command line. Some build systems, however, provide a graphical interface for editing the text files and invoking the build tool.
* The most common build tool is the `make` utility; the text files it relies on are called `makefiles`. While there are many versions of make, such as GNU make, the most powerful and portable make incarnation. `GNU make` is an extremely flexible tool that can be more than building C++ applications. It also has the advantage of being widely used and well-understood by developers. Unfortunately, getting GNU make to do exactly what you want it to do can be a `challenge`, especially with complex projects involving multiple toolsets. For that reason, I will also discuss Boost.Build, a powerful and extensible build system designed from the ground up for building C++ applications.
* `Boost.Build` was developed by members of the Boost C++ Libraries project. It has been used by a large community of developers for several years, and is currently under active development. Boost.Build uses a build tool called `bjam` and text files called `Jamfiles`. Its greatest strength is the ease with which it allows you to manage complex projects involving multiple platforms and build configurations. Although Boost.Build started out as an extension of Perforce’s Jam build system, it has since undergone extensive redesign.

## 工具集

**Names of command-line tools for various toolsets**

| Toolset | Compiler | Linker | Archiver |
| :-: | :-: | :-: | :-: |
| GCC | g++[.exe] | g++ | ar[.exe] |
| Visual C++ | cl.exe | link.exe | lib.exe |
| Intel (Windows) | icl.exe | xilink.exe | xilib.exe |
| Intel (Linux) | icpc | icpc | ar<br>ranlib |
| Metrowerks | mwcc[.exe] | mwld[.exe] | mwld[.exe] |
| Comeau | como[.exe] | como[.exe] | Toolset-dependent |
| Borland | bcc32.exe | bcc32.exe<br>ilink32.exe | tlib.exe |
| Digital Mars | dmc.exe | link.exe | lib.exe |

**Location of your command-line tools**

| Toolset | Location |
| :-: | :-: |
| GCC (Unix) | Typically /usr/bin or /usr/local/bin |
| GCC (Cygwin) | The bin subdirectory of your Cygwin installation |
| GCC (MinGW) | The bin subdirectory of your MinGW installation |
| Visual C++ | The VC/bin subdirectory of your Visual Studio installation |
| Intel (Windows) | The Bin subdirectory of your Intel compiler installation |
| Intel (Linux) | The bin subdirectory of your Intel compiler installation |
| Metrowerks | The Other Metrowerks Tools/Command Line Tools subdirectory of your CodeWarrior installation |
| Comeau | The bin subdirectory of your Comeau installation |
| Borland | The Bin subdirectory of your C++Builder, C++BuilderX or Borland command-line tools installation |

### The GNU Compiler Collection (GCC)

* GCC is a collection of compilers for a wide assortment of languages, including C and C++. It’s remarkable for being open source, available on almost every imaginable platform, and highly conformant to the C++ language standard. It’s the dominant compiler on many Unix platforms, and is also widely used on Microsoft Windows. You can learn a lot by compiling your code with GCC. If you think you know a way to improve the C++ language, you can test your idea with the GCC code base.
* GCC comes with libstdc++, a good open source implementation of the C++ standard library. It can also be used with the open source STLPort C++ standard library and with Dinkumware’s standard library.

### Visual C++

* Microsoft’s toolset is the dominant toolset on the Windows platform. While several old versions are still in wide use, the most recent version is highly standards conforming. It is also capable of producing highly optimized code. Microsoft’s tools are distributed with the Visual C++ and Visual Studio development environments. Visual C++ comes with a customized version of the Dinkumware C++ standard library implementation. Dinkumware’s C++ standard library is among the most efficient and standards-conforming commercial implementation.

## The Usage of GCC

### Building a Simple “Hello, World” Application from the Command Line

```bash
# Commands for compiling and linking hello.cpp in a single step
g++ -o hello hello.cpp
# Commands for compiling hello.cpp without linking
g++ -c -o hello.o hello.cpp
# Commands for linking hello
g++ -o hello hello.o
```

### Building a Static Library from the Command Line

```bash
# Commands for creating the archive libjohnpaul.lib or libjohnpaul.a
ar ru libjohnpaul.a john.o paul.o johnpaul.o
```

```bash
g++ -c -o john.o john.cpp
g++ -c -o paul.o paul.cpp
g++ -c -o johnpaul.o johnpaul.cpp
# The `ru` option tells `ar` to add the given object files to the specified archive if there are no existing archive members with the same names, but to update an existing archive member only if the given object file is newer than the existing member.
ar ru libjohnpaul.a john.o paul.o johnpaul.o
# Traditionally, after an archive was created or updated, the tool `ranlib` was used to create or update the archive’s symbol table, i.e., the index of the symbols that appear in the various object files it contains.
ranlib libjohnpaul.a
```

### Building a Dynamic Library from the Command Line

```bash
# GCC
g++ -shared -fPIC -o libgeorgeringo.so george.o ringo.o georgeringo.o
# GCC (Mac OS X)
g++ -dynamiclib -fPIC -o libgeorgeringo.dylib george.o ringo.o georgeringo.o
# GCC (Cygwin)
g++ -shared -o libgeorgeringo.dll -Wl,--out-implib,libgeorgeringo.dll.a -W1,--export-all-symbols -Wl,--enable-auto-image-base george.o ringo.o georgeringo.o
# GCC (MinGW)
g++ -shared -o libgeorgeringo.dll -Wl,--out-implib,libgeorgeringo.a -W1,--export-all-symbols -Wl,--enable-auto-image-base george.o ringo.o georgeringo.o
```

* Each command line specifies:
  * The name of the input files: george.obj, ringo.obj, and georgeringo.obj
  * The name of the dynamic library to be created
  * On Windows, the name of the import library
* `Some Unix linkers` should be told to generate position-independent code using the option `-fPIC` (GCC and Intel for Linux). This option makes it more likely that multiple processes will be able to share a single copy of the dynamic library’s code; on some systems, failing to specify this option can cause a linker error. Similarly, on Windows the GCC linker the option --enable-auto-image-base makes it less likely that the operating system will attempt to load two dynamic libraries at the same location; using this option helps to speed DLL loading.  
  
#### Symbol visibility

* `Dynamic libraries` can contain the definitions of classes, functions, and data. `On some platforms`, all such symbols are automatically accessible to code which uses a dynamic library; `other systems` offer programmers fine-grained control over which symbols are accessible. Being able to determine which symbols should be visible on a case-by-case basis is generally advantageous; it gives a programmer more explicit control of his library’s public interface, and it often provides superior performance. It also makes building and using dynamic libraries more complex, however.
* `With most Windows toolsets`, in order for a symbol defined in a dynamic library to be available to code which uses the dynamically library, `it must be explicitly exported when the dynamic library is built and imported when an executable or dynamic library that uses the dynamic library is built`. Some Unix toolsets also offer this flexibility; this is true for recent versions of GCC on several platforms, for Metrowerks on Mac OS X, and for Intel on Linux. In some cases, however, there is no alternative but to make all symbols visible.

#### Passing libraries to the linker

* `On Unix`, a dynamic library can be specified as input to the linker when code using the dynamic library is linked. `On Windows`, except when using GCC, dynamic libraries are not specified directly as input to the linker; instead, an import library or module definition file is used.

#### Import libraries and module definition files

* Import libraries, roughly speaking, are static libraries containing the information needed to invoke functions in a DLL at runtime. It’s not necessary to know how they work, only how to create and use them. Most linkers create import libraries automatically when you build a DLL, but in some cases it may be necessary to use a separate tool called an import librarian.
* A module definition file, or `.def` file, is a text file that describes the functions and data exported by a DLL. A `.def` file can be written by hand or automatically generated by a tool.

**A module definition file for libgeorgeringo.dll**
```
LIBRARY LIBGEORGERINGO.DLL

EXPORTS
    Georgeringo    @1
```

#### Exporting symbols from a DLL

* There are two standard methods for exporting symbols from a Windows DLL:
  * Use the `__declspec(dllexport)` attribute in the DLL’s headers, and build an import library for use when linking code that uses your DLL. <br>The `__declspec(dllexport)` attribute should be inserted at the beginning of the declarations of exported functions and data, following any linkage specifiers, and immediately following the class or struct keyword for exported classes. Note that `__declspec(dllexport)` is not part of the C++ language; `it is a language extension implemented by most Windows compilers`.
  * Create a .def file describing the functions and data exported by your dynamic library.

**Using the _ _declspec(dllexport) attribute**

```C++
__declpec(dllexport) int m = 3; // Exported data definition 
extern __declpec(dllexport) int n; // Exported data declaration 
__declpec(dllexport) void f(); // Exported function declaration 
class __declpec(dllexport) c { // Exported class definition
    /* ... */ 
};
```

* Using a `.def` file has certain advantages; for instance, it can allow functions in a DLL to be accessed by number rather than name, decreasing the size of a DLL. It also eliminates the need for the messy preprocessor directives. It has some serious `drawbacks`, however. For example, a `.def` file cannot be used to export classes. Furthermore, it can be difficult to remember to update your .def file when you add, remove, or modify functions in your DLL. I therefore `recommend` that you `always use __declspec(dllexport)`. To learn the full syntax of .def files as well as how to use them, consult your toolset’s documentation.

#### Importing symbols from a DLL

* There are two ways to import symbols:
  * In the headers included by source code that uses your DLL, use the attribute `__declspec(dllimport)` and pass an import library to the linker when linking code that uses your DLL.
  * Specify a `.def` file when linking code which depends on you DLL.

* Just as with exporting symbols, I `recommend` that you use the attribute `__declspec(dllimport)` in your source code instead of using .def files. The attribute __declspec(dllimport) is used exactly like the attribute __declspec(dllexport), discussed earlier. Like `__declspec(dllexport)`, `__declspec(dllimport)` is `not` part of the `C++ language`, but `an extension implemented by most Windows compilers`.
* If you choose to use __declspec(dllexport) and __declspec(dllimport), you must be sure to use `__declspec(dllexport)` when building your DLL and `__declspec(dllimport)` when compiling code that uses your DLL. One approach would be to use two sets of headers: one for building your DLL and the other for compiling code that uses your DLL. This is not satisfactory, however, since it is difficult to maintain two separate versions of the same headers.
* `Instead`, the usual approach is to define a macro that expands to __declspec(dllexport) when building your DLL and to __declspec(dllimport) otherwise. In Example, I used the macro GEORGERINGO_DECL for this purpose. On Windows, GEORGERINGO_DECL expands to __declspec(dllexport) if the macro GEORGERING_SOURCE is defined and to __declspec(dllimport) otherwise. By defining GEORGERING_SOURCE when building the DLL libgeorgeringo.dll but not when compiling code that uses libgeorgeringo.dll, you obtain the desired result.

**Example**

```C++
#ifndef GEORGERINGO_HPP_INCLUDED
#define GEORGERINGO_HPP_INCLUDED
// define GEORGERINGO_DLL when building libgerogreringo.dll 
# if defined(_WIN32) && !defined(__GNUC__)
#  ifdef GEORGERINGO_DLL
#   define GEORGERINGO_DECL __declspec(dllexport)
#  else
#   define GEORGERINGO_DECL __declspec(dllimport) 
#  endif
# endif // WIN32

#ifndef GEORGERINGO_DECL
# define GEORGERINGO_DECL
#endif

// Prints "George, and Ringo\n"
#ifdef __MWERKS__
# pragma export on
#endif

GEORGERINGO_DECL void georgeringo(); 
#ifdef __MWERKS__
# pragma export off
#endif

#endif // GEORGERINGO_HPP_INCLUDED
```

#### Building DLLs with GCC

* The Cygwin and MinGW ports of GCC, handle DLLs `differently` than other Windows toolsets. When you build a DLL with GCC, all functions, classes, and data are exported by default. This behavior can be modified by passing the option --no-export-all-symbols to the linker, by using the attribute __declspec(dllexport) in your source files, or by using a .def file. In each of these three cases, unless you use the option --export-all-symbols to force the linker to export all symbols, the only exported functions, classes, and data will be those marked __declspec(dllexport) or listed in the .def file.
* It’s therefore possible to use the GCC toolset to build DLLs in two ways: like an ordinary Windows toolset, exporting symbols explicitly using __declspec, or like a Unix toolset, exporting all symbols automatically. If you choose this method, you should consider using the option --export-all-symbols as a safety measure, in case you happen to include headers containing __declspec(dllexport).
* GCC differs from other Windows toolsets in a second way: rather than passing the linker an import library associated with a DLL, you can pass the DLL itself. This is usually faster than using an import library. It can also create problems, however, since several versions of a DLL may exist on your system, and you must ensure that the linker selects the correct version.

#### GCC 4.0’s -fvisibility option

* See C++ Cookbook 30 page

### Building a Complex Application from the Command Line

* Step
    * Start by building the static and dynamic libraries on which your application depends. Or use the third party libraries
    * Next, compile your application’s .cpp files into object files. You may need to use the -I option to tell your compiler where to search for the headers needed by your application
    * Finally, use your linker to produce an executable from the collection of object files and libraries. For each library, you must either provide a full pathname or tell the linker where to search for it
* At each stage of this process, if you are using a toolset which comes with static and dynamic variants of its runtime libraries, and if your program uses at least one dynamic library, you should direct the compiler or linker to use a dynamically linked runtime library

**Commands for linking the application hellobeatle.exe**

| Toolset | Input files | Command line |
| :-: | :-: | :-: |
| GCC (Unix) | hellobeatles.o <br>libjohnpaul.a <br>libgeorgeringo.so | g++ -o hellobeatles hellobeatles.o -L../johnpaul -L../georgeringo -ljohnpaul -lgeorgeringo <br>or <br>g++ -o hellobeatles hellobeatles.o ../johnpaul/libjohnpaul.a ../georgeringo/libgeorgeringo.so |
| GCC (Mac OS X) | hellobeatles.o <br>libjohnpaul.a <br>libgeorgeringo.dylib | g++ -o hellobeatles hellobeatles.o -L../johnpaul -L../georgeringo -ljohnpaul -lgeorgeringo<br>or<br>g++ -o hellobeatles hellobeatles.o ../johnpaul/libjohnpaul.a ../georgeringo/libgeorgeringo.dylib |
| GCC (Cygwin) | hellobeatles.o <br>libjohnpaul.a <br>libgeorgeringo.dll.a | g++ -o hellobeatles hellobeatles.o -L../johnpaul -L../georgeringo -ljohnpaul -lgeorgeringo<br>or<br>g++ -o hellobeatles hellobeatles.o ../johnpaul/libjohnpaul.a ../georgeringo/libgeorgeringo.dll.a |
| GCC (MinGW) | hellobeatles.o <br>libjohnpaul.a <br>libgeorgeringo.a | g++ -o hellobeatles hellobeatles.o -L../johnpaul -L../georgeringo -ljohnpaul -lgeorgeringo<br>or<br>g++ --o hellobeatles hellobeatles.o ../johnpaul/libjohnpaul.a ../georgeringo/libgeorgeringo.a |
| Visual C++ | hellobeatles.obj <br>libjohnpaul.lib <br>libgeorgeringo.lib | link -nologo -out:hellobeatles.exe -libpath:../johnpaul -libpath:../georgeringo libjohnpaul.lib libgeorgeringo.lib hellobeatles.obj |

* On both Windows and Unix, libraries can be passed to the linker in two ways:
    * By specifying a pathname on the command line
    * By specifying the simple name of the library together with a location to search for the library

> The locations to search for libraries can usually be specified on the command line. Most linkers use the option `-L<directory>` for this purpose, but Visual C++ use `-lipath:<directory>`

* The way the name of a library is specified to the linker differs between Unix and Windows. `On Windows`, the full name of the library is specified, including the file extension. `On Unix—and on Windows when using the GCC toolset—libraries` are specified using the -l option followed by the name of the library, with the file extension and the lib prefix removed. This means that the name of `a library must begin with lib to be automatically found by the linker`. More interestingly, it gives the linker the opportunity to choose between several versions of a library. If the linker finds both static and dynamic version of a library, the dynamic library is selected, unless otherwise specified. On some systems, the linker may choose between several versions of a dynamic library based on the portion of the file name following .so.
* Be aware that Unix linkers can be very sensitive to the order in which object files and static libraries are specified on the command line: if a static library or object file references a symbol defined in a second static library or object file, the first file must appear before the second file on the command line. To resolve circular dependencies, it is sometimes necessary to specify a given library or object file more than once. Another solution is to pass a sequence of object files and static libraries to linker bracketed by `-(` and `-)`; this causes the file to be searched repeatedly until all references are resolved. This option should be avoided if possible because it can significantly degrade performance.

#### Running your application

* If your application uses a dynamic variant of your toolset’s runtime library, the runtime library must be available when your application is run and in a location where it will be found automatically by the operating system’s dynamic loader. `Typically, this means that the dynamic runtime library must be placed either in the same directory as your application or in one of a list of system-specific directories.` This is more of a concern when developing for Windows than when developing for Unix, since on Unix the appropriate runtime libraries are often already installed in the correct locations.

# Boost.Build

## Build process

> `Jamfiles` and an interpreter called `b2`

* 每一个包含配置文件的目录都是一个项目, 如果这个目录中没有配置文件, 什么都不会发生.
* 当 `b2` 启动时, 它只在当前目录中搜索配置文件, 如果没有它不会做任何事情.
* `b2` 搜索的文件名为 `Jamfile.jam`. 如果在当前目录中找到了 `Jamfile`, 它将继续在父目录中搜索更多的 `Jamfile`. `b2` 向上搜索知道找到一个配置文件名为 `Jamroot.jam`. `Jamroot.jam` 和 `Jamfile.jam` 没有区别, 它仅仅用于指示 `b2` 不用再向上继续搜索了.
* `b2` 在父文件夹中搜索配置文件的原因是: 便于分组配置. 如果一些组件有相似的配置, 可以将相似的配置写入配置文件放入父文件夹中, 在子文件夹的组件构建时, 父文件夹的中配置将自动被使用
* 注意: `b2` 必须找到 `Jamroot.jam` 文件. 如果 `Jamroot.jam` 文件存在于当前文件夹下, 那么就不需要 `Jamfile.jam` 文件了. 如果 `Jamroot.jam` 文件在父文件夹下, 那么 `Jamfile.jam` 就必须存在于当前文件夹下, 否则 `b2` 不做任何事情
* 如果将 `b2` 复制到不包含 `Jamfile` 的目录，并启动程序，`b2` 将抛出找不到构建系统的错误. `b2` 首先做的是`加载构建系统`而不是搜索 `Jamfile`
* `b2` 是一个解释器(解释 `Jamfile`), 它并不知道怎么构建程序. `Boost.Build` 是 `Jamfile` 的真实执行者, `Jamfile` 包含使 `Boost.Build` 成为强大工具的所有执行逻辑.
* `b2` 仅仅读取 `Jamfile` 的内容, 所以它需要知道到哪里去寻找 `Jamfiles Boost.Build`
* `b2` 启动后, 首先在当前目录寻找 `boost-build.jam`, 如果没有找到就在所有的父文件夹. 这个文件中只需要告诉 `b2` 到什么地方去寻找构建系统 `boost-build /Users/Liu-Mac/CODE/C++/boost_1_65_1/tools/build/src ; `. 包含构建系统的文件中必须包含 `bootstrap.jam` 文件, 这就是 `b2` 加载构建系统需要的文件
* 如果启动 `b2` 时, 没有指定使用的工具集, `b2` 会自行检测并决定使用哪个工具集. 手动指定方法 `b2 toolset = gcc` or `b2 toolset = msvc`
* 一旦构建系统被发现, 加载, 锁定工具集, `b2` 在当前目录搜索 `Jamfile.jam` , 如果没有找到就抛出错误
* 如果你创建了一个空的 `Jamfile.jam`, 启动 `b2` 后, 另一个错误将抛出, `b2` 最终需要寻找一个叫 `Jamroot.jam`的 `Jamfile`
* 注意: 如果你的项目很小, 那么你只需要一个存放于当前目录的配置文件 `Jamroot.jam`.
* 构建过程总结:
    * 1. 在当前目录创建 `boost-build.jam` 文件, 用于指示 `构建系统` 地址, 保证构建系统目录中存在 `bootstrap.jam` 文件
    * 2. 编写 `Jamfiles`. 小项目: 直接在当前项目中创建 `Jamroot.jam` 文件; 大项目: 当前目录中创建 `Jamfile.jam`, 将各个组件公共的配置项, 抽出放入父目录的 `Jamfile.jam` 文件中, 工程根目录必须存在 `Jamroot.jam` 文件
    * 3. 启动 `b2` 程序, 进行构建 `b2 toolset = gcc`



| Toolset Name | Vendor | Notes |
| :-: | :-: | :-: |
| acc | Hewlett Packard | Only very recent versions are known to work well with Boost |
| borland | Borland |  |
| como | Comeau Computing | Using this toolset may require configuring another toolset to act as its backend. |
| darwin | Apple Computer | Apple's version of the GCC toolchain with support for Darwin and MacOS X features such as frameworks. |
| gcc | The Gnu Project | Includes support for Cygwin and MinGW compilers. |
| hp_cxx | Hewlett Packard | Targeted at the Tru64 operating system. |
| intel | Intel |  |
| msvc | Microsoft |  |
| sun | Oracle | Only very recent versions are known to work well with Boost. Note that the Oracle/Sun compiler has a large number of options which effect binary compatibility: it is vital that the libraries are built with the same options that your appliction will use. In particular be aware that the default standard library may not work well with Boost, unless you are building for C++11. The particular compiler options you need can be injected with the b2 command line options cxxflags=``and ``linkflags=. For example to build with the Apache standard library in C++03 mode use b2 cxxflags=-library=stdcxx4 linkflags=-library=stdcxx4. |
| vacpp | IBM | The VisualAge C++ compiler. |

## Basic tasks

> `Rules` and `features`

* `Boost.Build` 提供了很多内置的规则(函数). `exe` 就是最常用的一个.
* `Boost.Build` 基于的编程语言, 只有一种数据类型, 就是`字符串数组`. 数组可以为空或包含一个或多个字符串. 
* 函数调用的规则: 字符串如果有空格就要使用双引号包裹. 参数之间用 `:` 隔开, 函数调用结尾使用 `;`. 语句中, 严格使用空格隔开, `:` 左右, `;` 左侧.



**exe规则** 

```
exe hello : hello.cpp ; 
# 指定生成 `release` 版本, 默认是生成 `debug` 版本
exe hello : hello.cpp : <variant>release ; 
# `b2 variant = debug` 在上面的 Jamfile 下, 这条命令会报错.
# `exe` 的第四个参数包含默认使用, 但是可以被覆盖的功能
exe hello : hello.cpp : : <variant>release ; 
# 同时构建 `debug` `release` 版本
# 第四个参数值不能放在第三个参数, 这会抛出错误. 不能将互相排斥的值传入第三个参数
exe hello : hello.cpp : : <variant>debug <variant>release ; 
# 在 exe 中内置两个预处理指令 WIN32 、 _WIN32
# <define> 用于定义预处理指令
exe hello : hello.cpp : <define>WIN32 <define>_WIN32 : <variant>debug <variant>release ; 
# <define> 并不互斥, 所以这里将其放在第四个参数和第三个参数的唯一区别就是: 第四个参数的是默认值, 可以被覆盖丢弃, 第三个参数传递的任何东西是不可改变的
exe hello : hello.cpp : : <variant>debug <variant>release <define>WIN32 <define>_WIN32 ; 
# <optimization> 互斥. 所以这里会生成 2 * 2 (4) 个版本
exe hello : hello.cpp : : <variant>debug <variant>release <optimization>speed <optimization>off ; 
```

**lib规则**

```
# 构建动态链接库(默认)
lib world : world.cpp ; 
# 设置 <link> 标签为 static, 可以生成静态库
lib world : world.cpp : <link>static ; 
# 同时构建静态和动态链接库. 第三个和第四个参数的规则和 exe 一样
lib hello : hello.cpp : : <link>static <link>shared ; 
```

**install规则**

```
exe hello : hello.cpp ; 
# hello 是对第一个语句中的 hello 的引用
install "/Users/Liu-Mac/Desktop/bin" : hello ; 
# 使用 <locatin> 标签将安装目录放到第三个参数
# 将引用上一个语句的 hello 尽量放在前面的参数位置上
install install-bin : hello : <location>"/Users/Liu-Mac/Desktop/bin" ; 
# 通过 <target-os> 确定操作系统, 然后指定不同的安装目录
install install-bin : hello : <target-os>windows:<location>"C:/Program Files/hello" <target-os>linux:<location>/usr/local/bin ; 
```

**glob规则**

```
# glob 规则允许你使用通配符
# 这是一个嵌套的函数调用, glob 规则的结果作为 exe 规则的第二个参数传入. 嵌套调用的时候使用 `[` `]`
exe hello : [ glob *.cpp ] ; 
```

## Project management

> Multiple Jamfiles

## Best practices

> How Boost.Build is used by others

## Rule reference

> Building blocks for Jamfiles

## Feature reference

> Configuration options for the build process

[Boost.Build User Manual](http://www.boost.org/build/doc/html/index.html)


# GNU make

* 待续...

