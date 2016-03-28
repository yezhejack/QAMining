/****************************************************************************
** Meta object code from reading C++ file 'QtGnuplotWindow.h'
**
** Created by: The Qt Meta Object Compiler version 63 (Qt 4.8.7)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "QtGnuplotWindow.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'QtGnuplotWindow.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.7. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_QtGnuplotWindow[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       8,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      16,   42,   49,   49, 0x0a,
      50,   49,   49,   49, 0x0a,
      65,   49,   49,   49, 0x08,
      73,   49,   49,   49, 0x08,
      87,   49,   49,   49, 0x08,
     103,   49,   49,   49, 0x08,
     117,   49,   49,   49, 0x08,
     138,   49,   49,   49, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_QtGnuplotWindow[] = {
    "QtGnuplotWindow\0on_setStatusText(QString)\0"
    "status\0\0on_keyAction()\0print()\0"
    "exportToPdf()\0exportToImage()\0"
    "exportToSvg()\0showSettingsDialog()\0"
    "settingsSelectBackgroundColor()\0"
};

void QtGnuplotWindow::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        QtGnuplotWindow *_t = static_cast<QtGnuplotWindow *>(_o);
        switch (_id) {
        case 0: _t->on_setStatusText((*reinterpret_cast< const QString(*)>(_a[1]))); break;
        case 1: _t->on_keyAction(); break;
        case 2: _t->print(); break;
        case 3: _t->exportToPdf(); break;
        case 4: _t->exportToImage(); break;
        case 5: _t->exportToSvg(); break;
        case 6: _t->showSettingsDialog(); break;
        case 7: _t->settingsSelectBackgroundColor(); break;
        default: ;
        }
    }
}

const QMetaObjectExtraData QtGnuplotWindow::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject QtGnuplotWindow::staticMetaObject = {
    { &QMainWindow::staticMetaObject, qt_meta_stringdata_QtGnuplotWindow,
      qt_meta_data_QtGnuplotWindow, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &QtGnuplotWindow::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *QtGnuplotWindow::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *QtGnuplotWindow::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_QtGnuplotWindow))
        return static_cast<void*>(const_cast< QtGnuplotWindow*>(this));
    if (!strcmp(_clname, "QtGnuplotEventReceiver"))
        return static_cast< QtGnuplotEventReceiver*>(const_cast< QtGnuplotWindow*>(this));
    return QMainWindow::qt_metacast(_clname);
}

int QtGnuplotWindow::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QMainWindow::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 8)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 8;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
