/****************************************************************************
** Meta object code from reading C++ file 'QtGnuplotEvent.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "QtGnuplotEvent.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'QtGnuplotEvent.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_QtGnuplotEventHandler[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       5,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       2,       // signalCount

 // signals: signature, parameters, type, tag, flags
      22,   34,   34,   34, 0x05,
      35,   34,   34,   34, 0x05,

 // slots: signature, parameters, type, tag, flags
      50,   34,   34,   34, 0x08,
      66,   34,   34,   34, 0x08,
      78,   34,   34,   34, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_QtGnuplotEventHandler[] = {
    "QtGnuplotEventHandler\0connected()\0\0"
    "disconnected()\0newConnection()\0"
    "readEvent()\0connectionClosed()\0"
};

void QtGnuplotEventHandler::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        QtGnuplotEventHandler *_t = static_cast<QtGnuplotEventHandler *>(_o);
        switch (_id) {
        case 0: _t->connected(); break;
        case 1: _t->disconnected(); break;
        case 2: _t->newConnection(); break;
        case 3: _t->readEvent(); break;
        case 4: _t->connectionClosed(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData QtGnuplotEventHandler::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject QtGnuplotEventHandler::staticMetaObject = {
    { &QObject::staticMetaObject, qt_meta_stringdata_QtGnuplotEventHandler,
      qt_meta_data_QtGnuplotEventHandler, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &QtGnuplotEventHandler::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *QtGnuplotEventHandler::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *QtGnuplotEventHandler::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_QtGnuplotEventHandler))
        return static_cast<void*>(const_cast< QtGnuplotEventHandler*>(this));
    return QObject::qt_metacast(_clname);
}

int QtGnuplotEventHandler::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 5)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 5;
    }
    return _id;
}

// SIGNAL 0
void QtGnuplotEventHandler::connected()
{
    QMetaObject::activate(this, &staticMetaObject, 0, 0);
}

// SIGNAL 1
void QtGnuplotEventHandler::disconnected()
{
    QMetaObject::activate(this, &staticMetaObject, 1, 0);
}
QT_END_MOC_NAMESPACE
