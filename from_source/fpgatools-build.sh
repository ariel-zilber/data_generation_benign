#!/bin/bash
#
# Summon FPGA Tools build script
# Written by Piotr Esden-Tempski <piotr@esden.net>, released as public domain.
# Tool section
##############################################################################
TAR=tar

##############################################################################
# OS and Tooldetection section
# Detects which tools and flags to use
##############################################################################

case "$(uname)" in
	Linux)
	echo "Found Linux OS."
	;;
	Darwin)
	echo "Found Darwin OS."
	QT5_PREFIX="/usr/local/opt/qt5"
	PATH="/usr/local/opt/bison/bin:$PATH"
	LDFLAGS="-L/usr/local/opt/bison/lib"
	;;
	CYGWIN*)
	echo "Found CygWin that means Windows most likely."
	;;
	*)
	echo "Found unknown OS. Aborting!"
	exit 1
	;;
esac

##############################################################################
# Building section
# You probably don't have to touch anything after this
##############################################################################

##############################################################################
# Helper function definitions
##############################################################################

# Fetch a versioned file from a URL
function fetch {
    if [ ! -e ${STAMPS}/$1.fetch ]; then
        if [ ! -e ${SOURCES}/$1 ]; then
            log "Downloading $1 sources..."
			if [ "x$3" != "x" ]; then
				wget -c ${FETCH_NO_PASSIVE} ${FETCH_NO_CERTCHECK} -O $3 $2 && touch ${STAMPS}/$1.fetch
			else
				wget -c ${FETCH_NO_PASSIVE} ${FETCH_NO_CERTCHECK} $2 && touch ${STAMPS}/$1.fetch
			fi
        fi
    fi
}

function clone {
    local NAME=$1
    local GIT_REF=$2
    local GIT_URL=$3
    local POST_CLONE=$4
    local GIT_SHA=$(git ls-remote ${GIT_URL} ${GIT_REF} | cut -f 1)

    # It seems that the ref is actually a SHA as it could not be found through ls-remote
    if [ "x${GIT_SHA}" == "x" ]; then
        local GIT_SHA=${GIT_REF}
    fi

    # Setting uppercase NAME variable for future use to the source file name
    eval $(echo ${NAME} | tr "[:lower:]" "[:upper:]")=${NAME}-${GIT_SHA}

    # Clone the repository and do all necessary operations until we get an archive
    if [ ! -e ${STAMPS}/${NAME}-${GIT_SHA}.fetch ]; then
        # Making sure there is nothing in our way
        if [ -e ${NAME}-${GIT_SHA} ]; then
            log "The clone directory ${NAME}-${GIT_SHA} already exists, removing..."
            rm -rf ${NAME}-${GIT_SHA}
        fi
        log "Cloning ${NAME}-${GIT_SHA} ..."
        git clone --recursive ${GIT_URL} ${NAME}-${GIT_SHA}
        cd ${NAME}-${GIT_SHA}
        log "Checking out the revision ${GIT_REF} with the SHA ${GIT_SHA} ..."
        git checkout -b sft-branch ${GIT_SHA}
	if [ "x${POST_CLONE}" != "x" ]; then
		log "Running post clone code for ${NAME}-${GIT_SHA} ..."
		${POST_CLONE}
	fi
        log "Removing .git directory from ${NAME}-${GIT_SHA} ..."
        rm -rf .git
        # save git SHA for later (needed for libtrellis)
        echo ${GIT_SHA} > .git_sha
        cd ..
        log "Generating source archive for ${NAME}-${GIT_SHA} ..."
        tar cfj ${SOURCES}/${NAME}-${GIT_SHA}.tar.bz2 ${NAME}-${GIT_SHA}
        rm -rf ${NAME}-${GIT_SHA}
        touch ${STAMPS}/${NAME}-${GIT_SHA}.fetch
    fi
}

# Log a message out to the console
function log {
    echo "******************************************************************"
    echo "* $*"
    echo "******************************************************************"
}

# Unpack an archive
function unpack {
    log Unpacking $*
    # Use 'auto' mode decompression.  Replace with a switch if tar doesn't support -a
    ARCHIVE=$(ls ${SOURCES}/$1.tar.*)
    case ${ARCHIVE} in
	*.bz2)
	    echo "archive type bz2"
	    TYPE=j
	    ;;
	*.gz)
	    echo "archive type gz"
	    TYPE=z
	    ;;
	*)
	    echo "Unknown archive type of $1"
	    echo ${ARCHIVE}
	    exit 1
	    ;;
    esac
    ${TAR} xf${TYPE}${TARFLAGS} ${SOURCES}/$1.tar.*
}

# Install a build
function install-parallel {
    log $1
    ${SUDO} make ${PARALLEL} ${MAKEFLAGS} $2 $3 $4 $5 $6 $7 $8
}

function install {
    log $1
    ${SUDO} make ${MAKEFLAGS} $2 $3 $4 $5 $6 $7 $8
}

##############################################################################
# Create directories
##############################################################################

mkdir -p ${STAMPS} ${SOURCES}

cd ${SOURCES}

##############################################################################
# Fetch sources
##############################################################################

if [ ${ICESTORM_EN} != 0 ]; then
	if [ "x${ICESTORM_GIT}" == "x" ]; then
		log "There is no icestorm stable release download server yet!"
		exit 1
		#fetch ${ICESTORM} https://github.com/cliffordwolf/icestorm/archive/${ICESTORM}.tar.bz2
	else
		clone icestorm ${ICESTORM_GIT} git://github.com/cliffordwolf/icestorm.git
	fi
fi

if [ ${PRJTRELLIS_EN} != 0 ]; then
	if [ "x${PRJTRELLIS_GIT}" == "x" ]; then
		log "There is no prjtrellis stable release download server yet!"
		exit 1
		#fetch ${PRJTRELLIS} https://github.com/SymbiFlow/prjtrellis/archive/${PRJTRELLIS}.tar.bz2
	else
		clone prjtrellis ${PRJTRELLIS_GIT} git://github.com/SymbiFlow/prjtrellis.git
	fi
fi

#if [ ${ARACHNEPNR_EN} != 0 ]; then
#	if [ "x${ARACHNEPNR_GIT}" == "x" ]; then
#		log "There is no arachne-pnr stable release download server yet!"
#		exit 1
#		#fetch ${ARACHNEPNR} https://github.com/YosysHQ/arachne-pnr/archive/${ARACHNEPNR}.tar.bz2
#	else
#		clone arachnepnr ${ARACHNEPNR_GIT} git://github.com/YosysHQ/arachne-pnr.git
#	fi
#fi

if [ ${NEXTPNR_ICE40_EN} != 0 ] || [ ${NEXTPNR_ECP5_EN} != 0 ]; then
	if [ "x${NEXTPNR_GIT}" == "x" ]; then
		log "There is no nextpnr stable release download server yet!"
		exit 1
		#fetch ${NEXTPNR} https://github.com/YosysHQ/nextpnr/archive/${NEXTPNR}.tar.bz2
	else
		clone nextpnr ${NEXTPNR_GIT} git://github.com/YosysHQ/nextpnr.git
	fi
fi

if [ ${YOSYS_EN} != 0 ]; then
	if [ "x${YOSYS_GIT}" == "x" ]; then
		fetch ${YOSYS} https://github.com/YosysHQ/yosys/archive/${YOSYS}.tar.gz
	else
		clone yosys ${YOSYS_GIT} git://github.com/YosysHQ/yosys.git
	fi
fi

if [ ${IVERILOG_EN} != 0 ]; then
	if [ "x${IVERILOG_GIT}" == "x" ]; then
		fetch ${IVERILOG} https://github.com/steveicarus/iverilog/archive/${IVERILOG_VERSION}.tar.gz ${IVERILOG}.tar.gz
	else
		clone iverilog ${IVERILOG_GIT} git://github.com/steveicarus/iverilog.git
	fi
fi

##############################################################################
# Build tools
##############################################################################

cd ${SUMMON_DIR}

if [ ! -e build ]; then
    mkdir build
fi

if [ ${ICESTORM_EN} != 0 ] && [ ! -e ${STAMPS}/${ICESTORM}.build ]; then
    unpack ${ICESTORM}
    cd ${ICESTORM}
    log "Building ${ICESTORM}"
    make ${PARALLEL} ${MAKEFLAGS} PREFIX=${PREFIX}
    install-parallel ${ICESTORM} PREFIX=${PREFIX} install
    cd ..
    log "Cleaning up ${ICESTORM}"
    touch ${STAMPS}/${ICESTORM}.build
    rm -rf ${ICESTORM}
fi

if [ ${PRJTRELLIS_EN} != 0 ] && [ ! -e ${STAMPS}/${PRJTRELLIS}.build ]; then
    unpack ${PRJTRELLIS}
    cd ${PRJTRELLIS}/libtrellis
    log "Configuring ${PRJTRELLIS}"
    # need to set CURRENT_GIT_VERSION or libtrellis will try and fail
    # to detect the git revision (the .git directory is deleted before archiving)
    cmake -DCMAKE_INSTALL_PREFIX=${PREFIX} -DCURRENT_GIT_VERSION=$(< ../.git_sha) .
    log "Building ${PRJTRELLIS}"
    make ${PARALLEL} ${MAKEFLAGS}
    install-parallel ${PRJTRELLIS} install
    cd ../..
    log "Running post install tasks for ${PRJTRELLIS}"
    cd ${PREFIX}/share/trellis
    ${SUDO} ln -sf ../../lib/trellis libtrellis
    cd -
    log "Cleaning up ${PRJTRELLIS}"
    touch ${STAMPS}/${PRJTRELLIS}.build
    rm -rf build/* ${PRJTRELLIS}
fi

#if [ ${ARACHNEPNR_EN} != 0 ] && [ ! -e ${STAMPS}/${ARACHNEPNR}.build ]; then
#    unpack ${ARACHNEPNR}
#    cd ${ARACHNEPNR}
#    log "Building ${ARACHNEPNR}"
#    make ${PARALLEL} ${MAKEFLAGS} PREFIX=${PREFIX}
#    install-parallel ${ARACHNEPNR} PREFIX=${PREFIX} install
#    cd ..
#    log "Cleaning up ${ARACHNEPNR}"
#    touch ${STAMPS}/${ARACHNEPNR}.build
#    rm -rf ${ARACHNEPNR}
#fi

if { [ ${NEXTPNR_ICE40_EN} != 0 ] || [ ${NEXTPNR_ECP5_EN} != 0 ]; } && [ ! -e ${STAMPS}/${NEXTPNR}.build ]; then
    unpack ${NEXTPNR}
    cd build
    log "Configuring ${NEXTPNR}"
    CMAKE_PREFIX_PATH=${QT5_PREFIX:-${QT5_PREFIX}/lib/cmake/Qt5}
    cmake -DARCH="ice40;ecp5" -DCMAKE_INSTALL_PREFIX=${PREFIX} \
        -DCMAKE_PREFIX_PATH=${CMAKE_PREFIX_PATH} \
        -DBUILD_GUI=${NEXTPNR_BUILD_GUI} \
        -DTRELLIS_INSTALL_PREFIX=${PREFIX} \
        -DICEBOX_ROOT=${PREFIX}/share/icebox ../${NEXTPNR}
    log "Building ${NEXTPNR}"
    make ${PARALLEL} ${MAKEFLAGS}
    install-parallel ${NEXTPNR} install
    cd ..
    log "Cleaning up ${NEXTPNR}"
    touch ${STAMPS}/${NEXTPNR}.build
    rm -rf build/* ${NEXTPNR}
fi

if [ ${YOSYS_EN} != 0 ] && [ ! -e ${STAMPS}/${YOSYS}.build ]; then
    unpack ${YOSYS}
    if [ "x${YOSYS_GIT}" == "x" ]; then
        cd yosys-${YOSYS}
    else
        cd ${YOSYS}
    fi
    log "Building ${YOSYS}"
    make ${PARALLEL} ${MAKEFLAGS} ${YOSYSFLAGS} PREFIX=${PREFIX}
    install-parallel ${YOSYS} PREFIX=${PREFIX} install
    cd ..
    log "Cleaning up ${YOSYS}"
    touch ${STAMPS}/${YOSYS}.build
    if [ "x${YOSYS_GIT}" == "x" ]; then
        rm -rf yosys-${YOSYS}
    else
        rm -rf ${YOSYS}
    fi
fi

if [ ${IVERILOG_EN} != 0 ] && [ ! -e ${STAMPS}/${IVERILOG}.build ]; then
    unpack ${IVERILOG}
    cd ${IVERILOG}
    log "Running autogen for ${IVERILOG}"
    sh ./autoconf.sh
    cd ../build
    log "Configuring ${IVERILOG}"
    ../${IVERILOG}/configure --prefix=${PREFIX}
    log "Building ${IVERILOG}"
    make ${PARALLEL} ${MAKEFLAGS}
    install ${IVERILOG} install
    cd ..
    log "Cleaning up ${IVERILOG}"
    touch ${STAMPS}/${IVERILOG}.build
    rm -rf build/* ${IVERILOG}
fi
