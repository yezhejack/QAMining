/****************************************************************************
** Meta object code from reading C++ file 'QtGnuplotApplication.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "QtGnuplotApplication.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'QtGnuplotApplication.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_QtGnuplotApplication[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       4,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      21,   47,   54,   54, 0x0a,
      55,   54,   54,   54, 0x2a,
      73,   54,   54,   54, 0x0a,
      92,   54,   54,   54, 0x0a,

       0        // eod
};

static const char qt_meta_stringdata_QtGnuplotApplication[] = {
    "QtGnuplotApplication\0windowDestroyed(QObject*)\0"
    "object\0\0windowDestroyed()\0enterPersistMode()\0"
    "exitPersistMode()\0"
};

void QtGnuplotApplication::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        QtGnuplotApplication *_t = static_cast<QtGnuplotApplication *>(_o);
        switch (_id) {
        case 0: _t->windowDestroyed((*reinterpret_cast< QObject*(*)>(_a[1]))); break;
        case 1: _t->windowDestroyed(); break;
        case 2: _t->enterPersistMode(); break;
        case 3: _t->exitPersistMode(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData QtGnuplotApplication::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject QtGnuplotApplication::staticMetaObject = {
    { &QApplication::staticMetaObject, qt_meta_stringdata_QtGnuplotApplication,
      qt_meta_data_QtGnuplotApplication, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &QtGnuplotApplication::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *QtGnuplotApplication::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *QtGnuplotApplication::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_QtGnuplotApplication))
        return static_cast<void*>(const_cast< QtGnuplotApplication*>(this));
    if (!strcmp(_clname, "QtGnuplotEventReceiver"))
        return static_cast< QtGnuplotEventReceiver*>(const_cast< QtGnuplotApplication*>(this));
    return QApplication::qt_metacast(_clname);
}

int QtGnuplotApplication::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QApplication::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 4)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 4;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
