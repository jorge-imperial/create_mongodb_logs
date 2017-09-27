use test;

db.foo.insert( { field_a: '1', field_b: 'b', field_c: 0 });

var bulk = db.bar.initializeOrderedBulkOp();
bulk.insert( { field_a: '1', field_b : '17', field_c: 0 } );
bulk.insert( { field_a: '2', field_b : '16', field_c: 1 } );
bulk.insert( { field_a: '3', field_b : '15', field_c: 2 } );
bulk.insert( { field_a: '4', field_b : '14', field_c: 3 } );
bulk.insert( { field_a: '5', field_b : '13', field_c: 4 } );
bulk.insert( { field_a: '6', field_b : '12', field_c: 5 } );
bulk.insert( { field_a: '7', field_b : '11', field_c: 6 } );
bulk.insert( { field_a: '8', field_b : '10', field_c: 7 } );
bulk.insert( { field_a: '9', field_b : '9',  field_c: 8 } );
bulk.insert( { field_a: '10', field_b : '8', field_c: 9 } );
bulk.insert( { field_a: '11', field_b : '7', field_c: 10 } );
bulk.insert( { field_a: '12', field_b : '6', field_c: 11 } );
bulk.insert( { field_a: '13', field_b : '5', field_c: 12 } );
bulk.insert( { field_a: '14', field_b : '4', field_c: 13 } );
bulk.insert( { field_a: '15', field_b : '3', field_c: 14 } );
bulk.insert( { field_a: '16', field_b : '2', field_c: 15 } );
bulk.insert( { field_a: '17', field_b : '1', field_c: 16 } );
bulk.execute();

db.bar.findAndModify( { query: { field_c: 7 }, update: { $set : { field_c: 99 } }});

db.bar.createIndex( { field_a: 1 } );
db.bar.find( { field_a: '10' } );

db.bar.find( { field_b: '5' });

db.bar.count();

var col = db.bar;
var cur = col.find().batchSize(3);
cur.next();
cur.next();
cur.next();

db.bar.update({ field_a: '17' }, { field_b: 99, field_c: 99 }, { upsert: 1} );

db.bar.remove( { field_a: '3'});
